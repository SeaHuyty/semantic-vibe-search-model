# Vibe Search — Spotify Million Song Dataset

## Problem
Search 57,650 songs by natural-language *vibe* / mood / aesthetic (not keyword, not genre tag).
Dataset = lyrics + metadata only (artist, song, link, text). No audio features.

## Approach
Semantic search: embed lyrics and queries into the same vector space, rank by similarity.
Pretrained sentence embedding model used **out of the box** — no fine-tuning.

---

## Architecture

```
OFFLINE (build once)
┌─────────────┐   ┌──────────────┐   ┌───────────────┐   ┌────────────────┐
│ raw CSV      │──▶│ clean + chunk│──▶│ embed + mean-  │──▶│ song_embeddings │
│ 57,650 songs │   │ lyrics       │   │ pool per song  │   │ .pkl index      │
└─────────────┘   └──────────────┘   └───────────────┘   └────────────────┘

ONLINE (per query)
┌───────────────┐   ┌───────────────┐   ┌─────────────────┐   ┌──────────────┐
│ user query     │──▶│ embed query   │──▶│ cosine similarity│──▶│ top-K ranked │
│ (CLI, free text)│  │ (same model)  │   │ vs all 57,650    │   │ results table│
└───────────────┘   └───────────────┘   └─────────────────┘   └──────────────┘
```

Pipeline files:
| File | Role |
|---|---|
| `scripts/prepare_dataset.py` | clean lyrics, chunk into windows |
| `inference.py` | build embedding index + interactive CLI search |
| `evaluate.py` | qualitative check — fixed test queries, eyeball relevance |
| `configs/network_configs.yml` | model name, chunk size, paths, top-K |

---

## Model: Sentence-Transformers `all-MiniLM-L6-v2`

| Model | Dims | Speed | Vibe quality | Note |
|---|---|---|---|---|
| **all-MiniLM-L6-v2** (used) | 384 | fastest (~5x MPNet) | good baseline | chosen for speed + low resource cost |
| all-mpnet-base-v2 | 768 | slower | best quality | fallback if quality insufficient |
| bge-small-en-v1.5 | 384 | fast | slightly > MiniLM | alt fallback |

Swappable via one config key (`model.base_model`) — no code change.

---

## Design Q&A

**Embedding dimension & representation**
- 384-dim, `all-MiniLM-L6-v2` (Sentence-Transformers, pretrained, frozen).
- Long lyrics → chunked into 200-word windows (30-word overlap) → each chunk embedded → mean-pooled into one 384-dim vector per song.

**Similarity metric**
- Cosine similarity. Standard for Sentence-Transformer embedding space, invariant to vector magnitude.

**Indexing strategy**
- Brute-force / flat search over all 57,650 vectors.
- 57,650 × 384-dim ≈ 90MB — exact search is <100ms on CPU.
- No ANN index (HNSW/IVF) needed at this scale; revisit only if corpus grows 10x+.

**Storage**
- Single `.pkl`: `{embeddings: np.ndarray, metadata: pd.DataFrame}`, row-aligned.

---

## Results (sample)
| Query | Top result | Score |
|---|---|---|
| christmas holiday cheer song | Christmas Songs — Christmas Day | 0.65 |
| aggressive high-energy hype music | Judas Priest — Metal Meltdown | 0.51 |
| sad piano song about losing someone | Nightwish — Dead Boy's Poem | 0.62 |
| chill lo-fi vibe for studying | (weak match) | 0.44 |

Score doubles as a confidence signal — low scores (<0.5) correctly indicate no strong match exists in the dataset (e.g. dataset predates lo-fi genre), rather than a false-confident bad result.

## Known limitations
- No audio/instrumentation signal — lyrics-only, so instrument-specific queries ("piano", "acoustic") are silently ignored.
- Dataset skews older — modern genre slang (lo-fi, etc.) underrepresented.
- Pretrained model is general-purpose, not music/emotion-specific — no fine-tuning done yet (future option if quality insufficient).
