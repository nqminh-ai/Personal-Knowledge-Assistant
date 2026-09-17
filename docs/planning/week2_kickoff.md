# Week 2 Kickoff

Week 2 starts after the corpus v0 and environment smoke tests are available.

## Entry criteria

- `pip install -r requirements.txt` completes in the project environment.
- `scripts/sanity_embedding.py` passes on the local machine.
- `scripts/sanity_llm.py` passes with one configured provider, or is explicitly marked blocked by the team.
- At least 25 source documents are collected locally under `data/raw/`.
- Each source document has a metadata record under `data/metadata/`.

## Tasks

| Owner | Task | Output |
| --- | --- | --- |
| A | Collect and inventory 25-30 documents; flag scans and difficult layouts | `data/raw/`, metadata records |
| B | Build a first parser/chunker and embedding notebook | parsed chunks and embedding timing |
| C | Implement prompt/context assembly and citation parsing | generation module draft |
| D | Create 30-50 pilot QA items from the collected corpus | evaluation seed file |
| E | Review reproducibility, privacy, and experiment logging | QA notes and run checklist |

## Week 2 exit criteria

- One reproducible ingestion run produces chunks with stable `doc_id`, page, and `chunk_id`.
- One retrieval query returns inspectable top-k chunks.
- One grounded answer includes citations or abstains when evidence is missing.
