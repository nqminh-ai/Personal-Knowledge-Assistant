# Personal Knowledge Assistant

Personal Knowledge Assistant is a research-driven RAG system for asking grounded questions over a personal learning corpus. The project focuses on measurable retrieval and generation quality, not only a chatbot demo.

## Goals

- Ingest PDF, DOCX, PPTX, and scanned documents with metadata.
- Build reproducible retrieval baselines: Dense, BM25 with Vietnamese word segmentation, Hybrid, and Hybrid + Reranker.
- Generate grounded answers with citations and abstention when evidence is missing.
- Evaluate retrieval, answer quality, faithfulness, citation correctness, latency, and cost.
- Produce a final report, benchmark logs, and an end-to-end demo.

## Repository Structure

```text
personal-knowledge-assistant/
├── configs/            # Versioned project decisions and experiment configs
├── data/
│   ├── raw/            # Source documents, ignored by git except .gitkeep
│   ├── processed/      # Parsed/cleaned/chunked data, ignored by git
│   ├── indexes/        # FAISS/BM25/vector indexes, ignored by git
│   └── evaluation/     # Evaluation sets and outputs, ignored by git
├── docs/
│   ├── planning/       # Plans, weekly checklists, decision logs
│   └── research/       # Research notes for model/tool choices
├── idea/               # Original HTML planning documents
├── notebooks/          # Exploratory notebooks
└── src/
    ├── ingestion/      # Parsing, OCR, cleaning, metadata
    ├── retrieval/      # Embeddings, FAISS, BM25, hybrid, reranker
    ├── generation/     # Prompting, context assembly, API
    └── evaluation/     # Metrics, RAGAS/NLI, reports
```

## Week 1 Deliverables

- `docs/planning/week1_data_collection_plan.md`
- `docs/research/week1_embedding_vectorstore_research.md`
- `docs/research/week1_llm_prompt_research.md`
- `docs/planning/week1_evaluation_schema.md`
- `configs/project_decisions.yaml`

## Setup

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

API keys must stay in `.env` and must not be committed.

## Roles

- A - Data & Ingestion: corpus, parsing, OCR, metadata, Vietnamese word segmentation.
- B - Retrieval Engineer: embeddings, vector store, BM25, hybrid retrieval, reranking.
- C - LLM/RAG Engineer: prompts, context assembly, citations, abstention.
- D - Evaluation & Frontend: metrics, evaluation set, dashboards.
- E - Research/PM/QA: research questions, protocol, QA, report, integration.
