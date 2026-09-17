# Implementation Plan

## Goal
Semantic "vibe" search over the Spotify Million Song Dataset. User types a natural-language mood/aesthetic description; the system returns the most semantically similar songs by lyrics content, ranked by cosine similarity, served through a CLI.

## Design decisions (locked in)
- **Embedding model**: pretrained Sentence-Transformers encoder used **out of the box as a frozen feature extractor** — starting with `all-MiniLM-L6-v2` (384-dim). No fine-tuning, no training pipeline. Query text and lyrics text are embedded with the same frozen model, relying on its pretrained semantic space to place similar "vibes" close together.

### Base encoder candidates

| Model | Dims | Encoding Speed | Vibe/Aesthetic Search Quality | Best For |
|---|---|---|---|---|
| `all-MiniLM-L6-v2` (chosen) | 384 | Fastest (~5x MPNet) | Good — solid semantic baseline | Rapid prototyping, weak GPU/CPU, fast offline batch embedding |
| `all-mpnet-base-v2` | 768 | Slower | Best overall quality | Abstract themes, emotional nuance, complex artistic metaphor |
| `bge-small-en-v1.5` | 384 | Fast | Slightly higher retrieval accuracy than MiniLM | Small memory footprint while matching modern retrieval benchmarks |

Starting with `all-MiniLM-L6-v2` for the first working pipeline (speed, low resource cost, easy iteration). If retrieval quality on abstract/metaphorical queries proves weak, swap to `all-mpnet-base-v2` (quality-max) or `bge-small-en-v1.5` (same speed class, better benchmark accuracy) — one-line config change (`model.base_model` in `network_configs.yml`), no code change since the model is loaded directly via `sentence-transformers`.
- **Long lyrics handling**: chunk lyrics into fixed-size windows (respecting the encoder's token limit), embed each chunk, mean-pool into one song-level vector.
- **Similarity metric**: cosine similarity — standard for Sentence-Transformer embeddings, invariant to embedding magnitude.
- **Indexing**: brute-force / flat search over all ~57k song vectors. At this scale (57k × 384-dim ≈ 90MB) exact search is fast enough (<100ms) on CPU; no ANN index (HNSW/IVF) needed yet.
- **Storage**: single `.pkl` holding `{embeddings: np.ndarray, metadata: pd.DataFrame}` (artist, song, link, lyrics), row-aligned by index. Simplicity over portability at this scale.
- **CLI**: build with Typer + Rich (typed args, nice table output for ranked results).

## Scope pivot (locked in)
No training. Pretrained encoder used purely for inference/feature extraction. Dropped from the project: `networks.py`, `losses.py`, `train.py`, `metrices.py`, `data_generator.py` (were training-pipeline files — contrastive fine-tuning on synthetic VADER-tagged vibe labels; abandoned in favor of the frozen pretrained encoder). `evaluate.py` kept but repurposed as a qualitative check (manual test queries + eyeballed relevance), since there's no held-out labeled retrieval set without a training pipeline.

## Per-file responsibilities

### `scripts/prepare_dataset.py`
- Load `data/spotify_millsongdata.csv`.
- Clean lyrics text: strip newlines/control chars, drop empty/near-empty lyric rows, normalize whitespace.
- Chunk lyrics per song (fixed word window, default 200 words, 30-word overlap).
- Output: cleaned dataframe (`artist`, `song`, `link`, `lyrics_clean`, `chunks: list[str]`) saved to `data/processed/songs_processed.pkl`.
- **Status: done.**

### `inference.py` (CLI deliverable)
- Indexing step: load `songs_processed.pkl`, embed each song's chunks with the frozen pretrained encoder, mean-pool per song into one vector, save `{embeddings, metadata}` to the `.pkl` index (`configs.index.embeddings_path`). Build once, reuse across CLI runs (skip rebuild if index file already exists, unless `--rebuild` passed).
- Interactive Typer/Rich CLI: accept a free-text vibe query, embed it with the same frozen encoder, cosine-similarity search (brute-force) against the saved `.pkl` index, print top-K ranked results (artist, song, similarity score) in a Rich table.

### `evaluate.py`
- Qualitative sanity check only (no training, no ground-truth labels): run a small fixed set of example vibe queries (e.g. "melancholic acoustic ballad for a rainy morning", "aggressive high-energy hype music") through the same search path as `inference.py`, print top-K results per query for manual eyeballing of relevance.

### `configs/network_configs.yml`
- Central config: base model name, embedding dim, chunk size/overlap, index/output paths. Training-related keys (`train:`, `pairs:`) to be pruned since no training pipeline remains.

### `requirements.txt`
- `sentence-transformers`, `torch` (backend dep of sentence-transformers), `pandas`, `numpy`, `pyyaml`, `typer`, `rich`. `tqdm` kept for embedding-progress bar during index build. `vaderSentiment` no longer needed (was for the dropped training pipeline) — remove.

## Build order
1. `requirements.txt` — done, prune `vaderSentiment` if unused going forward.
2. `configs/network_configs.yml` — done, prune training-only keys.
3. `scripts/prepare_dataset.py` — done.
4. `inference.py` — build index (embed + save `.pkl`) + interactive CLI search.
5. `evaluate.py` — qualitative test-query script, once `inference.py` search path exists to reuse.

Each file gets built and smoke-tested individually before moving to the next (component-basis testing per best_practice.md #6).
