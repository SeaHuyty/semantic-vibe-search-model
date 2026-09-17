import argparse

import pandas as pd
from sentence_transformers import SentenceTransformer

from inference import build_index, load_config, print_results, search_index

TEST_QUERIES = [
    "melancholic acoustic ballad for a rainy morning",
    "aggressive high-energy hype music",
    "romantic slow dance song",
    "nostalgic summer road trip anthem",
    "dark brooding song about heartbreak",
]


def main():
    parser = argparse.ArgumentParser(description="Qualitative vibe-search evaluation")
    parser.add_argument("--config", type=str, default="configs/network_configs.yml")
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
