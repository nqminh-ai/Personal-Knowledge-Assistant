# Week 1 LLM and Prompt Research

Owner: C - LLM/RAG Engineer

## Objective

Pick candidate LLM providers and define prompt/citation behavior before backend implementation starts.

## LLM Candidates

| Candidate | Strength | Risk | Initial Use |
| --- | --- | --- | --- |
| OpenAI low-cost model | Stable API, good instruction following | Paid API | Primary candidate if API key is available |
| Gemini Flash | Low cost, large context, good speed | Provider differences in output style | Cost fallback |
| Qwen API/local | Cost control, open model options | More setup and quality variance | Research fallback |

## Prompt v0

```text
You are a personal knowledge assistant. Answer the user's question using only the provided CONTEXT.

Rules:
1. Do not use outside knowledge.
2. If the context does not contain enough evidence, say that you cannot find enough information in the provided documents.
3. Cite every factual claim using [doc_id, page, chunk_id].
4. Keep the answer concise and faithful to the source.

CONTEXT:
{context}

QUESTION:
{question}
```

## Citation Format v0

```text
[doc_id, page, chunk_id]
```

Example:

```text
Gradient descent updates parameters in the opposite direction of the gradient [doc_0004, p.12, chunk_0031].
```

## Week 2 Test

- Test one API call from a local script.
- Log latency, approximate token count, and cost if available.
- Test one no-answer question to verify abstention behavior.
