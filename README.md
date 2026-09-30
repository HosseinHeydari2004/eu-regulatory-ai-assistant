# EU Regulatory AI Assistant
 
An agentic RAG (Retrieval-Augmented Generation) system that answers questions about EU regulatory text — starting with Article 5 of the EU AI Act — with source-grounded answers and an LLM-as-judge verification step. Built as an end-to-end Applied AI Engineer portfolio project.
 
## Project Structure
 
* **`rag.py`** — the core pipeline: chunking, vector storage/retrieval (`retrieve()`), grounded answer generation (`generate_answer()`), and answer verification (`verify_answer()`). A single `ask_llm()` function is the one place the code talks to a language model, so swapping models later is a one-function change.
* **`eval_set.py`** — the 20-case evaluation set (15 answerable questions covering every chunk, 5 deliberately unanswerable).
* **`run_eval.py`** — runs the full pipeline against `eval_set.py` and prints retrieval accuracy, refusal accuracy, and groundedness rate.
* **`try_it.py`** — a minimal script for asking a single question and inspecting the answer/verdict, useful for quick manual checks.
* **`exploration.ipynb`** — the original development notebook. Kept as a record of the build process (including debugging real issues along the way), not the code that actually runs — `rag.py` is the current, canonical pipeline.
* **`data/`** — source documents (currently `ai_act_article5.txt`, from the EU AI Act, Regulation (EU) 2024/1689, via [EUR-Lex](https://eur-lex.europa.eu/eli/reg/2024/1689/oj/eng)).
## What's Included
 
### Foundations — embeddings and similarity
* Implemented cosine similarity from scratch with NumPy and verified it against library output before relying on any library-provided version.
### RAG pipeline — chunking, vector storage, and retrieval
* Article 5 is split into chunks based on its real lettered structure, embedded, and stored in a persistent Chroma vector database.
* `retrieve(query, n)` returns ranked, relevant chunks with distance scores.
### Generation — grounded answers with a local LLM
* `generate_answer(query, n)` retrieves relevant chunks and generates an answer constrained to only that context, returning both the answer and the context used.
### Agents — verification of generated answers
* `verify_answer(answer, context)` uses a second, independent LLM call (an LLM-as-judge pattern) to check whether every claim in a generated answer is actually supported by its context, returning a `GROUNDED` / `NOT_GROUNDED` verdict.
* Validated against a true positive (a correct, grounded answer) and a true negative (a fabricated penalty amount, correctly caught as unsupported).
### Evaluation — a systematic test set, and two real bugs it caught
* A 20-case evaluation set replaced hand-picked testing, and surfaced two real defects:
  * **A chunking bug**: the source document has two independently lettered lists at different structural levels; the original chunking flattened both together. Fixed by validating matches against the article's real structure. Retrieval accuracy improved from 86.7% to 100%.
  * **A verifier blind spot**: correct refusals ("I don't know") were being judged unsupported. Fixed with an explicit prompt instruction.
  * A related fix: the verifier's raw output format varied between runs (capitalization, line breaks, punctuation), requiring more defensive parsing than a naive first-line split.
* **Final scorecard, reproducible across multiple runs**: 100% retrieval accuracy, 100% refusal accuracy, 100% groundedness rate.
* Known limitation: chunk_8 (real-time biometric identification) is significantly larger than the other chunks, since that section of the article is long. It retrieved correctly for all six evaluation questions targeting it, but remains a candidate for further sub-chunking.
### Refactor — from notebook to a reusable module
* Moved the working pipeline out of the notebook into `rag.py`, with file paths made relative (no more machine-specific absolute paths) and the LLM call isolated behind `ask_llm()`.
* Re-ran the full 20-case evaluation against the refactored module as a regression test, confirming the same 100% / 100% / 100% scorecard.
## Setup
 
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```
 
This project also requires [Ollama](https://ollama.com) installed separately (not a pip package), with the Mistral model pulled locally:
 
```bash
ollama pull mistral
```
 
To build the index and try a question:
 
```bash
python try_it.py
```
 
To run the full evaluation:
 
```bash
python run_eval.py
```
 
## Roadmap
 
* Point `ask_llm()` at a hosted LLM API (in progress) to enable a live, deployed demo, since a deployed app can't reach a local Ollama instance.
* Attempt a live deployment (Streamlit Community Cloud), with a recorded demo video as a fallback if free-tier hosting constraints block it.
* Sub-chunk the oversized chunk_8 to test whether retrieval precision improves further.
* Formalize retrieve → generate → verify as a LangChain/LangGraph agent graph.
---
 
This project is actively evolving as I learn more about embeddings, retrieval systems, and RAG workflows.