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

### RAG pipeline — document chunking

* Loaded Article 5 (Prohibited AI Practices) of the EU AI Act into the project
* Split the article into coherent chunks using regex — one chunk per lettered sub-point (a)-(l), plus a separate intro chunk
* Verified chunk boundaries preserve complete, meaningful ideas rather than cutting text arbitrarily

**Source document:** EU AI Act, Regulation (EU) 2024/1689, via [EUR-Lex](https://eur-lex.europa.eu/eli/reg/2024/1689/oj/eng).

## Data

Raw source documents live in `data/`. Currently includes:

* `ai_act_article5.txt` — Article 5 of the EU AI Act, used as the source text for chunking and (soon) retrieval experiments

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

After installation, open `similarity.ipynb` and run the notebook cells.

## Roadmap

Planned next steps include:

* Storing chunk embeddings in a vector database (Chroma) and querying it for relevant chunks
* Adding an agentic layer: retrieval, reasoning, and a citation-verification step
* Building an evaluation set to measure retrieval accuracy and hallucination rate
* Deploying a live demo and adding monitoring/tracing

---

This project is actively evolving as I learn more about embeddings, retrieval systems, and RAG workflows.

