# Embedding Practice
 
This repository contains my early experiments with text embeddings and retrieval-augmented generation (RAG), building toward an end-to-end Applied AI Engineer portfolio project: an agentic assistant for EU regulatory documents.
 
## What's Included
 
### Foundations — embeddings and similarity
 
* Loaded a pretrained Sentence Transformer model (`all-MiniLM-L6-v2`)
* Generated 384-dimensional sentence embeddings
* Compared embeddings using the built-in `model.similarity()` method
* Implemented cosine similarity from scratch with NumPy
* Verified that the custom implementation produces results consistent with the library output
* Built a small ranking exercise: given a query sentence, rank other sentences by similarity
### RAG pipeline — chunking, vector storage, and retrieval
 
* Loaded Article 5 (Prohibited AI Practices) of the EU AI Act into the project
* Split the article into chunks using regex based on its lettered sub-points
* Embedded chunks and stored them in a persistent Chroma vector database
* Compared L2 and cosine distance metrics — confirmed they produce identical rankings for normalized embeddings (related by a fixed scaling factor)
* Investigated a retrieval ranking discrepancy and traced it to query phrasing
* Wrapped the full query pipeline into a reusable `retrieve(query, n=3)` function returning `(chunk_id, document, distance)` per result
### Generation — grounded answers with a local LLM
 
* Set up Mistral running locally via Ollama, separate from the embedding model used for retrieval
* Built a `generate_answer(query, n=3)` function that retrieves relevant chunks, inserts them into an instruction-constrained prompt, and generates an answer using only that context, returning both the answer and the context used
* Tested grounding behavior deliberately on an unrelated question and a topically-close but unanswerable question — confirmed correct refusal in both cases rather than hallucination
### Agents — verification of generated answers
 
* Built a `verify_answer(answer, context)` function using an LLM-as-judge pattern: a second model call checks whether every claim in a generated answer is supported by the retrieved context, returning a `GROUNDED` / `NOT_GROUNDED` verdict plus an explanation
* Tested the verifier against a true positive (a correct, grounded answer) and a true negative (a deliberately fabricated claim — a specific, plausible penalty amount not present anywhere in the source text) — both correctly classified
### Evaluation — a systematic test set, and two real bugs it caught
 
* Built a 20-case evaluation set (15 answerable questions covering every chunk, 5 deliberately unanswerable) to measure the pipeline systematically instead of relying on hand-picked examples
* **Found and fixed a chunking bug**: Article 5 contains two independently lettered lists at different structural levels — the top-level prohibited practices (a)-(h), and a nested 2-item sub-list inside a later paragraph that reuses the same `(a)`/`(b)` labels. The original regex-based chunking treated every lettered match as equivalent, corrupting several chunks. Fixed by validating each match against the article's known real structure (the correct sequence of top-level letters) rather than trusting pattern-matching alone, and rebuilt the vector database on the corrected 9-chunk structure. **Retrieval accuracy improved from 86.7% to 100%** as a direct, measured result.
* **Found and fixed a verifier blind spot**: the LLM-as-judge correctly assessed content-based answers but initially misjudged correct refusals ("I don't know") as unsupported rather than recognizing an accurate absence-of-information statement as itself grounded. Fixed with an explicit instruction in the verification prompt telling the judge to treat accurate refusals as `GROUNDED`.
* **Found and fixed output-parsing fragility**: the verifier's raw output format varied between runs (capitalization of the verdict word, whether the explanation appeared on the same line or a new one, trailing punctuation), which caused inconsistent scoring between otherwise-identical runs. Fixed with more defensive parsing that checks how the first line *starts* rather than trusting an exact format.
* **Final scorecard, confirmed reproducible across multiple runs**: 100% retrieval accuracy, 100% refusal accuracy, 100% groundedness rate.
* A known, documented limitation: chunk_8 (real-time biometric identification) absorbed significantly more content than any other chunk during the chunking fix, since the corresponding article section is long. Despite this, it retrieved correctly for all six evaluation questions pointing to it — but it remains a candidate for further sub-chunking in future work.
**Source document:** EU AI Act, Regulation (EU) 2024/1689, via [EUR-Lex](https://eur-lex.europa.eu/eli/reg/2024/1689/oj/eng).
 
## Data
 
Raw source documents live in `data/`. Currently includes:
 
* `ai_act_article5.txt` — Article 5 of the EU AI Act, used as the source text for chunking and retrieval
Generated vector database files live in `vector_store/` (not tracked in git — reproducible by re-running the notebook).
 
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
 
After installation, open `similarity.ipynb` and run the notebook cells.
 
## Roadmap
 
Planned next steps include:
 
* Sub-chunking the oversized chunk_8 to test whether retrieval precision improves further
* Introducing LangChain/LangGraph to formalize the retrieve → generate → verify pipeline as an orchestrated agent graph
* Deploying a live demo (FastAPI + Gradio/Streamlit, on Hugging Face Spaces) and adding monitoring/tracing
---
 
This project is actively evolving as I learn more about embeddings, retrieval systems, and RAG workflows.