#  Retrieval-Augmented Generation (RAG) System

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![LangChain](https://img.shields.io/badge/LangChain-1C3C3C?style=for-the-badge&logo=langchain&logoColor=white)](https://www.langchain.com/)
[![Vector DB](https://img.shields.io/badge/Vector%20Store-Chroma-FF4F8B?style=for-the-badge)](#)

# My Experiments & Learning

A hands-on sandbox repository to explore and understand the fundamentals of **Retrieval-Augmented Generation (RAG)**.

The goal of this repo is to experiment with document chunking, embeddings, vector search, and prompting LLMs with custom retrieved context.

---

## What's Inside

- **Document Ingestion & Chunking:** Testing different chunk sizes and overlaps on sample text/PDFs.
- **Embeddings & Vector Search:** Generating embeddings and running similarity searches using a local vector store.
- **Prompt Augmentation:** Injecting retrieved context chunks into LLM prompts to see how response accuracy improves.

---

## Tech Used

- **Language:** Python
- **Orchestration:** LangChain
- **Document Processing:** PyMuPDF 
- **Vector Store:** ChromaDB
- **LLM & Inference:** Groq API
- **Embeddings:** HuggingFace (`sentence-transformers`)

---

## 🏗️ System Architecture

```text
               ┌──────────────────────────┐
               │    Document Ingestion    │
               │ (PDF, Markdown, TXT, ...)│
               └────────────┬─────────────┘
                            │
                     [Text Splitter]
                            │
               ┌────────────▼─────────────┐
               │     Embedding Model      │
               └────────────┬─────────────┘
                            │
                     [Vector Embeddings]
                            │
               ┌────────────▼─────────────┐
               │      Vector Database     │
               └────────────┬─────────────┘
                            │
User Query ──► [Embed Query]│ (Top-K Similar Chunks)
                            ▼
              ┌───────────────────────────┐
              │    Prompt Construction    │
              │  (Query + Context Chunks) │
              └─────────────┬─────────────┘
                            │
              ┌─────────────▼─────────────┐
              │        LLM Engine         │
              └─────────────┬─────────────┘
                            │
                            ▼
                     Grounded Response

```
## Setup & Try
### 1. Clone the repo
```bash
git clone [https://github.com/DevDreamer26/RAG.git](https://github.com/DevDreamer26/RAG.git)
cd RAG
---
