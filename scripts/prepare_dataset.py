import argparse
import re
from pathlib import Path

import pandas as pd
import yaml

def load_config(config_path: str) -> dict:
    with open(config_path, "r") as f:
        return yaml.safe_load(f)


def clean_lyrics(text: str) -> str:
    text = text.replace("\\n", " ").replace("\n", " ").replace("\r", " ")
    text = re.sub(r"\s+", " ", text).strip()
    return text


def chunk_text(text: str, chunk_size: int, overlap: int) -> list[str]:
    words = text.split()
    if not words:
        return []
    chunks = []

    step = chunk_size - overlap
    for start in range(0, len(words), step):
        chunk = words[start:start + chunk_size]
        if chunk:
            chunks.append(" ".join(chunk))
        if start + chunk_size >= len(words):
            break
    return chunks


def process_dataset(input_path: str, output_path: str, cfg: dict) -> pd.DataFrame:
    df = pd.read_csv(input_path)

    df["lyrics_clean"] = df["text"].astype(str).apply(clean_lyrics)

    df = df[df["lyrics_clean"].str.len() >= cfg["data"]["min_lyrics_length"]]

    df["chunks"] = df["lyrics_clean"].apply(
        lambda t: chunk_text(
            t,
            chunk_size=cfg["data"]["chunk_size"],
            overlap=cfg["data"]["chunk_overlap"],
        )
    )
    df = df[df["chunks"].map(len) > 0]

    result = df[["artist", "song", "link", "lyrics_clean", "chunks"]].reset_index(drop=True)

    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    result.to_pickle(output_path)
    return result


def main():
    parser = argparse.ArgumentParser(description="Clean and chunk lyrics dataset")
    parser.add_argument("--config", type=str, default="configs/network_configs.yml")
    parser.add_argument("--input", type=str, default=None)
    parser.add_argument("--output", type=str, default=None)
    args = parser.parse_args()

    cfg = load_config(args.config)
    input_path = args.input or cfg["data"]["raw_csv"]
    output_path = args.output or f"{cfg['data']['processed_dir']}/songs_processed.pkl"

    df = process_dataset(input_path, output_path, cfg)

    print(f"Processed {len(df)} songs -> {output_path}")
    print(f"Avg chunks/song: {df['chunks'].map(len).mean():.2f}")


if __name__ == "__main__":
    main()