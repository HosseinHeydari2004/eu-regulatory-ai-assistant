# Embedding Practice

This repository contains my early experiments with text embeddings and retrieval-augmented generation (RAG). The goal is to understand the core concepts and build a solid foundation before developing a larger end-to-end project.

## What's Included

### `similarity.ipynb`

The main notebook currently covers:

* Loading a pretrained Sentence Transformer model (`all-MiniLM-L6-v2`)
* Generating 384-dimensional sentence embeddings
* Comparing embeddings using the built-in `model.similarity()` method
* Implementing cosine similarity from scratch with NumPy
* Verifying that the custom implementation produces results consistent with the library output

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

After installation, open `similarity.ipynb` and run the notebook cells.

## Roadmap

Planned next steps include:

* Exploring vector databases and similarity search
* Document chunking strategies
* Building a simple retrieval pipeline
* Developing a complete RAG application

---

This project is actively evolving as I learn more about embeddings, retrieval systems, and RAG workflows.

