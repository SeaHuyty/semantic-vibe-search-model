import argparse

import pandas as pd
from sentence_transformers import SentenceTransformer

from inference import build_index, load_config, print_results, search_index

TEST_QUERIES = [
    "happy anniversary",
    "party anthem for a Friday night club",
    "sad piano song about losing someone",
    "chill lo-fi vibe for studying",
    "christmas holiday cheer song",
    "motivational workout gym anthem",
    "patriotic song about war and sacrifice",
    "khmer song 2026",
    "modern k-pop dance track",
    "traditional cambodian wedding music",
    "tiktok viral dance sound 2026",
]


def main():
    parser = argparse.ArgumentParser(description="Qualitative vibe-search evaluation")
    parser.add_argument("--config", type=str, default="configs/network_configs_mpnet.yml")
    parser.add_argument("--top-k", type=int, default=None)
    args = parser.parse_args()

    cfg = load_config(args.config)
    build_index(cfg, force_rebuild=False)

    model = SentenceTransformer(cfg["model"]["base_model"])
    index = pd.read_pickle(cfg["index"]["embeddings_path"])
    k = args.top_k or cfg["eval"]["top_k"][-1]

    for query in TEST_QUERIES:
        print(f"\nQuery: \"{query}\"")
        results = search_index(query, model, index, k)
        print_results(results)


if __name__ == "__main__":
    main()
