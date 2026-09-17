# Week 1 Embedding and Vector Store Research

Owner: B - Retrieval Engineer

## Objective

Choose a simple, reproducible retrieval MVP for dense search, then leave room for BM25, hybrid retrieval, and reranking.

## Embedding Candidates

| Candidate | Strength | Risk | Initial Verdict |
| --- | --- | --- | --- |
| `BAAI/bge-m3` | Multilingual, strong retrieval baseline, supports Vietnamese reasonably well | Heavier than small SBERT models | Recommended MVP |
| Vietnamese SBERT variants | Lightweight and Vietnamese-focused | Quality varies by checkpoint/domain | Keep as fallback benchmark |
| OpenAI embedding API | Easy integration, strong baseline | Costs money, external dependency | Useful comparison if budget allows |

## Vector Store Candidates

| Candidate | Strength | Risk | Initial Verdict |
| --- | --- | --- | --- |
| FAISS | Local, fast, reproducible, no service needed | Less production-friendly metadata filtering | Recommended MVP |
| Qdrant | Service-based, better metadata/filtering, production-like | Requires Docker/service setup | Upgrade path |

## Recommended Week 1 Decision

- Dense embedding: `BAAI/bge-m3`.
- Vector store: FAISS.
- Sparse baseline: BM25 with Vietnamese word segmentation.
- Fusion: Reciprocal Rank Fusion in Week 6.

## Sanity Test for Week 2

Use 5-10 Vietnamese paragraph/query pairs and manually inspect whether nearest chunks are semantically plausible before committing to a full index.
