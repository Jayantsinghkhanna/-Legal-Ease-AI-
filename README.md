# ⚖️ Legal-Ease AI

<div align="center">

### 🧠 Graph-Assisted Hybrid RAG for Legal Contract Intelligence

Analyze • Understand • Summarize • Retrieve • Reason

Built using **Hybrid Retrieval**, **Knowledge Graphs**, **Cross-Encoder Re-Ranking**, and **LLMs** to deliver accurate, grounded, and explainable legal contract analysis.

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red)
![RAG](https://img.shields.io/badge/RAG-Hybrid-green)

![LLM](https://img.shields.io/badge/LLM-Gemini_2.5_Flash-orange)
![FAISS](https://img.shields.io/badge/FAISS-Vector_Search-blue)
![Knowledge Graph](https://img.shields.io/badge/Knowledge-Graph-yellow)

</div>

---

# 🚀 What is Legal-Ease AI?

Legal-Ease AI is an advanced Legal AI platform that transforms complex legal contracts into structured, searchable, and explainable knowledge.

Unlike traditional RAG systems that rely solely on vector search, Legal-Ease combines:

✅ Hybrid Retrieval  
✅ Knowledge Graphs  
✅ Cross-Encoder Re-Ranking  
✅ Contract Summarization  
✅ Legal Risk Analysis  
✅ Grounded Legal Question Answering  

to provide highly accurate contract intelligence.

---

# 🎯 Problem Statement

Legal contracts are:

- Long
- Complex
- Difficult to search
- Filled with legal jargon
- Time-consuming to review

Traditional chatbots often:

❌ Miss important clauses  
❌ Hallucinate answers  
❌ Ignore relationships between entities  
❌ Struggle with legal reasoning  

Legal-Ease solves these challenges using a **Graph-Assisted Hybrid RAG architecture**.

---

# ✨ Key Features

## 📄 Legal Contract Understanding

- Upload legal PDF contracts
- Automatic contract parsing
- Clause-aware chunking
- Contract type detection
- Party identification
- Important date extraction

---

## 🔍 Hybrid Retrieval

Combines:

### Semantic Search

Uses:

```text
FAISS + BGE Embeddings
```

to understand meaning.

Example:

```text
"How can this agreement end?"
```

can retrieve:

```text
Termination Clause
```

even when the exact wording is different.

---

### Keyword Search

Uses:

```text
BM25
```

for lexical matching.

Example:

```text
termination notice
```

retrieves clauses containing those exact keywords.

---

### Cross Encoder Re-Ranking

Uses:

```text
cross-encoder/ms-marco-MiniLM-L-6-v2
```

to rank retrieved clauses by relevance.

This significantly improves answer quality.

---

## 🧠 Knowledge Graph Construction

Legal-Ease automatically extracts:

- Parties
- Obligations
- Responsibilities
- Deadlines
- Compliance Requirements
- Legal Relationships

Example:

```text
Employee
     ↓
Provide Notice
     ↓
45 Days
```

The graph enables relationship-aware legal reasoning.

---

## ⚠️ Legal Risk Analysis

Detects:

- Missing Clauses
- Liability Risks
- Compliance Issues
- Ambiguous Language
- Contract Weaknesses

Provides:

```text
Risk Score
+
Risk Explanation
```

for faster legal review.

---

## 📑 Contract Summarization

Generates:

- Executive Summary
- Key Clauses
- Important Dates
- Governing Law
- Contract Type
- Parties

within seconds.

---

## 💬 Legal Question Answering

Ask questions like:

```text
What is the notice period?

Who is liable for damages?

What compliance requirements exist?

Who are the contracting parties?

Summarize this agreement.
```

Legal-Ease retrieves evidence before generating answers.

---

# 🏗️ System Architecture

```text
                    LEGAL-EASE AI

                Upload Legal PDF
                         │
                         ▼
                PDF Extraction
                         │
                         ▼
                Legal Parsing
                         │
                         ▼
             Clause-Based Chunking
                         │
                         ▼
                BGE Embeddings
                         │
                         ▼
              FAISS Vector Store
                         │
                         │
                         ├──────────────┐
                         │              │
                         ▼              ▼
               Semantic Search      BM25 Search
                         │              │
                         └──────┬───────┘
                                ▼
                      Hybrid Retrieval
                                │
                                ▼
                    Cross Encoder Reranker
                                │
                                ▼
                    Knowledge Graph Context
                                │
                                ▼
                       Gemini 2.5 Flash
                                │
                                ▼
      ┌────────────────────────────────────────┐
      │                                        │
      ▼                                        ▼
 Contract QA                         Risk Analysis

      ▼                                        ▼

 Summarization                    Legal Insights
```

---

# 🔥 Why This Is Not Traditional RAG

Traditional RAG:

```text
Query
 ↓
Vector Search
 ↓
LLM
```

Legal-Ease:

```text
Query
 ↓
FAISS Semantic Search
 +
BM25 Keyword Search
 ↓
Hybrid Retrieval
 ↓
Cross Encoder Re-Ranking
 ↓
Knowledge Graph Context
 ↓
Gemini 2.5 Flash
 ↓
Grounded Legal Answer
```

This produces significantly more accurate legal responses.

---

# 🧠 Knowledge Graph Example

Contract Clause:

```text
Employee must provide
45 days written notice.
```

Extracted Knowledge:

```json
{
  "party": "Employee",
  "obligation": "Provide Notice",
  "deadline": "45 Days",
  "clause_type": "Termination"
}
```

Graph Representation:

```text
Employee
    │
    ▼
Provide Notice
    │
    ▼
45 Days
```

This relationship becomes available during question answering.

---

# ⚡ Retrieval Pipeline

## Step 1

Semantic Retrieval

```text
FAISS
+
BGE Embeddings
```

---

## Step 2

Lexical Retrieval

```text
BM25
```

---

## Step 3

Hybrid Fusion

```text
Semantic Results
+
Keyword Results
```

---

## Step 4

Cross Encoder Re-Ranking

Ranks results based on actual relevance.

---

## Step 5

Graph Context Injection

Injects:

```text
Parties
Obligations
Deadlines
Relationships
```

into the final prompt.

---

## Step 6

LLM Reasoning

Powered by:

```text
Gemini 2.5 Flash
```

for answer generation.

---

# 🛠️ Tech Stack

## AI / LLM

- Gemini 2.5 Flash

## Embeddings

- BAAI/bge-base-en-v1.5

## Retrieval

- FAISS
- BM25
- Hybrid Retrieval

## Re-Ranking

- Cross Encoder
- ms-marco-MiniLM-L-6-v2

## Knowledge Graph

- NetworkX

## Backend

- Python

## Frontend

- Streamlit

## Data Validation

- Pydantic

## PDF Processing

- PyMuPDF

---

# 📂 Project Structure

```bash
legal-ease-v2/
│
├── app.py
│
├── src/
│   │
│   ├── ingestion/
│   │   ├── pdf_loader.py
│   │   └── legal_parser.py
│   │
│   ├── chunking/
│   │   └── clause_chunker.py
│   │
│   ├── retrieval/
│   │   ├── embedding_service.py
│   │   ├── faiss_store.py
│   │   ├── bm25_store.py
│   │   ├── hybrid_retriever.py
│   │   └── reranker.py
│   │
│   ├── legal_kg/
│   │   ├── legal_extractor.py
│   │   ├── kg_builder.py
│   │   └── kg_retriever.py
│   │
│   ├── llm/
│   │   ├── legal_chain.py
│   │   └── legal_qa.py
│   │
│   ├── summarization/
│   │   ├── contract_summarizer.py
│   │   ├── risk_analyzer.py
│   │   └── summary_models.py
│   │
│   └── evaluation/
│
├── requirements.txt
│
└── README.md
```

---

# 📊 Current Architecture Classification

| Component | Status |
|------------|---------|
| Traditional RAG | ✅ |
| Hybrid RAG | ✅ |
| Cross Encoder Re-Ranking | ✅ |
| Knowledge Graph Extraction | ✅ |
| Graph Context Injection | ✅ |
| Legal Risk Analysis | ✅ |
| Contract Summarization | ✅ |
| Full GraphRAG | 🚧 Future Work |

---

# 🚀 Future Enhancements

### Full GraphRAG

- Graph Traversal Retrieval
- Community Detection
- Graph-Based Search

### Multi-Document Legal Reasoning

Compare:

- Contract V1
- Contract V2
- Vendor Agreements

and identify differences automatically.

---

### Agentic Legal Review

Multiple AI Agents:

- Risk Agent
- Compliance Agent
- Clause Agent
- Negotiation Agent

working together.

---

### Legal Citation Engine

Generate:

```text
Answer
↓
Clause Reference
↓
Page Number
↓
Evidence
```

for explainable legal AI.

---

# 💼 Resume Description

> Built Legal-Ease AI, a Graph-Assisted Hybrid RAG platform for legal contract intelligence using FAISS, BM25, Cross-Encoder Re-Ranking, Knowledge Graphs, BGE Embeddings, Gemini 2.5 Flash, and Streamlit, enabling contract summarization, risk analysis, and grounded legal question answering.

---

# 👨‍💻 Author

### Jayant Singh Khanna

Machine Learning Intern | Generative AI Enthusiast

Interested in:

- Generative AI
- Agentic AI
- Knowledge Graphs
- GraphRAG
- Machine Learning
- MLOps
- Legal AI

---

# ⭐ If you found this project interesting, consider giving it a star!

**Legal-Ease AI — Making Legal Contracts Understandable Through AI.**
