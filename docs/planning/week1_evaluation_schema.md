# Week 1 Evaluation Schema

Owner: D - Evaluation & Frontend

## Objective

Define the evaluation item format before the team starts writing QA seed questions.

## Evaluation Item Schema v0

| Field | Description | Required |
| --- | --- | --- |
| question_id | Stable question id, for example `q_0001` | Yes |
| question | User-facing question | Yes |
| gold_answer | Short expected answer | Yes for answerable questions |
| gold_chunk_ids | One or more supporting chunks | Yes for answerable questions |
| doc_ids | Source documents that support the answer | Yes for answerable questions |
| query_type | One of the six query types below | Yes |
| difficulty | easy, medium, hard | Yes |
| is_answerable | true/false | Yes |
| notes | Ambiguity, expected behavior, annotation comments | No |

## Query Types

- `direct_lookup`: asks for explicit information.
- `semantic`: asks using paraphrase or conceptual wording.
- `keyword_heavy`: depends on exact terms, symbols, names, or formulas.
- `multi_document`: needs evidence from at least two documents or chunks.
- `conversational`: follow-up question that depends on prior context.
- `no_answer`: intentionally not answerable from the corpus.

## Example Rows

| question_id | question | gold_answer | gold_chunk_ids | doc_ids | query_type | difficulty | is_answerable |
| --- | --- | --- | --- | --- | --- | --- | --- |
| q_0001 | What is gradient descent used for? | Optimizing model parameters by minimizing a loss function. | chunk_0031 | doc_0004 | direct_lookup | easy | true |
| q_0002 | Which materials discuss evaluation metrics? | Requires combining notes from the ML evaluation slide and project proposal. | chunk_0012; chunk_0088 | doc_0002; doc_0007 | multi_document | hard | true |
| q_0003 | What is the final exam date? | N/A | N/A | N/A | no_answer | easy | false |

## Week 2 Gate

The QA seed can start when this schema is accepted by E/PM and all annotators understand the six query types.
