## Overview
Develop a semantic search engine using the Spotify Million Song Dataset (spotify_millsongdata.csv). The engine enables users to search for tracks by describing the "vibe", emotional mood, or aesthetic of a song in natural language (e.g., "melancholic acoustic ballad for a rainy morning" or "aggressive high-energy hype music").

## Dataset Details
  - Source: Kaggle — Spotify Million Song Dataset
  - File: spotify_millsongdata.csv (~57,650 tracks)
  - Schema:
    - artist: Artist name
    - song: Track title
    - link: Track link or path
    - text: Song lyrics
*** Note: Because this dataset contains lyrics and metadata rather than raw audio or acoustic features, your vibe-search strategy will rely on semantic text representations, sentiment/mood modeling, or lyrics-to-vibe embeddings. ***

## Deliverables
Interface for your implementation:

  - Command Line Interface (CLI)
    - An interactive terminal client (built using tools such as argparse, Typer, Click, or Rich).
    - Accepts descriptive text queries from standard input and outputs formatted, ranked search results directly to the console.

## Technical Architecture & Discussion
Be prepared to document and address the following design choices during evaluation:

  - Embedding Dimension & Representation
    - What is the dimensionality of your embedding vectors?
    - Which embedding model or feature-extraction strategy was used (e.g., Sentence Transformers, dense retrieval models, TF-IDF + SVD) to map user queries and lyrics into the same latent space?
    - How did you handle long lyric sequences (e.g., chunking, pooling, truncating, or summarization)?

  - Similarity Metric
    - Which similarity metric was selected (e.g., Cosine Similarity, Dot Product, Euclidean Distance)?
    - Justify why this metric is appropriate for your embedding space and normalization scheme.

  - Indexing Strategy
    - Which vector indexing approach did you implement (e.g., Brute-force/Flat, HNSW, IVF)?
    - Justify your selection considering the trade-offs between search latency, retrieval recall, and memory usage over the ~57k song collection.

## Getting Started
Download spotify_millsongdata.csv from Kaggle.
Preprocessing, Embedding Generation, and Initial Load
Build the interface to run your search (either a web page or a cli)