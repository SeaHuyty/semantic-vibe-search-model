# Implementation Plan

## Goal
Semantic "vibe" search over the Spotify Million Song Dataset. User types a natural-language mood/aesthetic description; the system returns the most semantically similar songs by lyrics content, ranked by cosine similarity, served through a CLI.

## Design decisions (locked in)
- **Embedding model**: Sentence-Transformers base encoder — starting with `all-MiniLM-L6-v2` (384-dim) — fine-tuned with a contrastive objective on (lyrics-chunk, vibe-description) pairs, so the query space and the lyrics space are trained to align — not just relying on off-the-shelf pretrained similarity. Base model is swappable via `configs/network_configs.yml`; candidates evaluated below.

### Base encoder candidates

| Model | Dims | Encoding Speed | Vibe/Aesthetic Search Quality | Best For |
|---|---|---|---|---|
| `all-MiniLM-L6-v2` (chosen) | 384 | Fastest (~5x MPNet) | Good — solid semantic baseline | Rapid prototyping, weak GPU/CPU, fast offline batch embedding |
| `all-mpnet-base-v2` | 768 | Slower | Best overall quality | Abstract themes, emotional nuance, complex artistic metaphor |
| `bge-small-en-v1.5` | 384 | Fast | Slightly higher retrieval accuracy than MiniLM | Small memory footprint while matching modern retrieval benchmarks |

Starting with `all-MiniLM-L6-v2` for the first working pipeline (speed, low resource cost, easy iteration). If retrieval quality on abstract/metaphorical queries proves weak during evaluation, swap to `all-mpnet-base-v2` (quality-max) or `bge-small-en-v1.5` (same speed class, better benchmark accuracy) — swap is a one-line config change since the encoder is wrapped in `networks.py` behind the config's `base_model` key.
- **Long lyrics handling**: chunk lyrics into fixed-size windows (respecting the encoder's token limit), embed each chunk, mean-pool into one song-level vector.
- **Similarity metric**: cosine similarity — matches the contrastive training objective and is invariant to embedding magnitude.
- **Indexing**: brute-force / flat search over all ~57k song vectors. At this scale (57k × 384-dim ≈ 90MB) exact search is fast enough (<100ms) on CPU; no ANN index (HNSW/IVF) needed yet.
- **Storage**: single `.pkl` holding `{embeddings: np.ndarray, metadata: pd.DataFrame}` (artist, song, link, lyrics), row-aligned by index. Simplicity over portability at this scale.
- **CLI**: build with Typer + Rich (typed args, nice table output for ranked results).

## Per-file responsibilities

### `scripts/prepare_dataset.py`
- Load `data/spotify_millsongdata.csv`.
- Clean lyrics text: strip newlines/control chars, dedupe repeated chorus blocks if needed, drop empty/near-empty lyric rows, normalize whitespace.
- Chunk lyrics per song (fixed token window, e.g. 128–256 tokens, slight overlap).
- Output: cleaned dataframe (`artist`, `song`, `link`, `lyrics_clean`, `chunks: list[str]`) saved to `data/processed/` for downstream use.

### `data_generator.py`
- Build the training pair set for contrastive fine-tuning: for each song (or chunk), generate a short "vibe description" label — either via a rule-based sentiment/mood tagger (e.g. VADER + keyword heuristics) or an LLM-generated paraphrase of the song's emotional tone.
- Emit `(lyrics_chunk, vibe_text, label)` triples — positive pairs (same song) and sampled negatives (different songs) — as a PyTorch `Dataset`/`DataLoader`.

### `networks.py`
- Define the model: a Sentence-Transformer encoder wrapped with an optional projection head (linear layer down to target embedding dim), shared weights for both "lyrics" and "query" inputs (bi-encoder / Siamese setup).

### `losses.py`
- Contrastive loss (e.g. InfoNCE or cosine-embedding triplet loss) operating on paired batch embeddings.

### `metrices.py`
- Retrieval evaluation metrics: Recall@K, MRR, mean cosine similarity of positive pairs vs. negatives — used both during training (validation) and in `evaluate.py`.

### `train.py`
- argparse CLI (per best_practice.md): `--lr`, `--batch-size`, `--epochs`, `--checkpoint-dir`, etc.
- Custom training loop (no `model.fit`), `tqdm` progress bar, checkpointing + best-so-far tracking based on validation metric from `metrices.py`.

### `evaluate.py`
- Load best checkpoint, run held-out evaluation set through `metrices.py`, report Recall@K / MRR.

### `inference.py` (CLI deliverable)
- On first run (or via a separate indexing step): embed all cleaned/chunked lyrics with the trained encoder, mean-pool per song, save to the `.pkl` index (embeddings + metadata).
- Interactive Typer/Rich CLI: accept a free-text vibe query, embed it with the trained encoder, cosine-similarity search (brute-force) against the saved `.pkl` index, print top-K ranked results (artist, song, similarity score) in a Rich table.

### `configs/network_configs.yml`
- Central config: base model name, embedding dim, chunk size/overlap, projection head dims, training hyperparameters, paths (data, checkpoints, index file).

### `requirements.txt`
- `sentence-transformers`, `torch`, `pandas`, `numpy`, `tqdm`, `typer`, `rich`, `pyyaml`, (`nltk`/`vaderSentiment` if rule-based mood tagging used for `data_generator.py`).

## Build order
1. `requirements.txt` — pin deps first.
2. `configs/network_configs.yml` — central knobs before code references them.
3. `scripts/prepare_dataset.py` — clean + chunk raw CSV.
4. `data_generator.py` — build training pairs from cleaned data.
5. `networks.py` — model definition.
6. `losses.py` — loss function.
7. `metrices.py` — eval metrics (needed by both train and evaluate).
8. `train.py` — training loop + checkpointing.
9. `evaluate.py` — held-out evaluation.
10. `inference.py` — build the `.pkl` index + interactive CLI search.

Each file gets built and smoke-tested individually before moving to the next (component-basis testing per best_practice.md #6).
