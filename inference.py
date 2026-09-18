from pathlib import Path

import numpy as np
import pandas as pd
import typer
import yaml
from rich.console import Console
from rich.table import Table
from sentence_transformers import SentenceTransformer
from tqdm import tqdm

app = typer.Typer()
console = Console()

def load_config(config_path: str = "configs/network_configs.yml") -> dict:
    with open(config_path, "r") as f:
        return yaml.safe_load(f)


def build_index(cfg: dict, force_rebuild: bool = False) -> None:
    index_path = Path(cfg["index"]["embeddings_path"])
    if index_path.exists() and not force_rebuild:
        console.print(f"[yellow]Index already exists at {index_path}, skipping build.[/yellow]")
        return

    processed_path = f"{cfg['data']['processed_dir']}/songs_processed.pkl"
    df = pd.read_pickle(processed_path)

    model = SentenceTransformer(cfg["model"]["base_model"])

    song_vectors = []

    for chunks in tqdm(df["chunks"], desc="Embedding songs", total=len(df)):
        chunk_embeddings = model.encode(chunks, convert_to_numpy=True, show_progress_bar=False)
        song_vector = chunk_embeddings.mean(axis=0)
        song_vectors.append(song_vector)

    embeddings = np.vstack(song_vectors)
    metadata = df[["artist", "song", "link"]].reset_index(drop=True)

    index_path.parent.mkdir(parents=True, exist_ok=True)
    pd.to_pickle({"embeddings": embeddings, "metadata": metadata}, index_path)

    console.print(f"[green]Built index: {embeddings.shape[0]} songs, {embeddings.shape[1]}-dim[/green]")


def search_index(query: str, model: SentenceTransformer, index: dict, top_k: int) -> pd.DataFrame:
    embeddings = index["embeddings"]
    metadata = index["metadata"]

    query_vec = model.encode([query], convert_to_numpy=True)[0]

    query_norm = query_vec / np.linalg.norm(query_vec)
    embeddings_norm = embeddings / np.linalg.norm(embeddings, axis=1, keepdims=True)

    scores = embeddings_norm @ query_norm

    top_indices = np.argsort(-scores)[:top_k]

    results = metadata.iloc[top_indices].copy()
    results["score"] = scores[top_indices]
    return results.reset_index(drop=True)


def print_results(results: pd.DataFrame) -> None:
    table = Table(title="Search Results")
    table.add_column("Rank", justify="right")
    table.add_column("Artist")
    table.add_column("Song")
    table.add_column("Score", justify="right")

    for i, row in results.iterrows():
        table.add_row(str(i + 1), row["artist"], row["song"], f"{row['score']:.4f}")

    console.print(table)


@app.command("build-index")
def cli_build_index(
    config: str = typer.Option("configs/network_configs.yml"),
    rebuild: bool = typer.Option(False, "--rebuild"),
):
    cfg = load_config(config)
    build_index(cfg, force_rebuild=rebuild)


@app.command("search")
def cli_search(
    query: str = typer.Option(None, "--query"),
    config: str = typer.Option("configs/network_configs.yml"),
    top_k: int = typer.Option(None, "--top-k"),
):
    cfg = load_config(config)
    build_index(cfg, force_rebuild=False)

    model = SentenceTransformer(cfg["model"]["base_model"])
    index = pd.read_pickle(cfg["index"]["embeddings_path"])
    k = top_k or cfg["index"]["top_k_results"]

    if query:
        results = search_index(query, model, index, k)
        print_results(results)
    else:
        console.print("[bold]Vibe search — type a query, or 'quit' to exit[/bold]")
        while True:
            q = typer.prompt("Query")
            if q.strip().lower() in ("quit", "exit"):
                break
            results = search_index(q, model, index, k)
            print_results(results)


if __name__ == "__main__":
    app()