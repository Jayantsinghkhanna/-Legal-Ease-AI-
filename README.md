# ⚖️ Legal-Ease AI
### Understand contracts. Find evidence. Review risks.

<div align="center">

**Graph-Assisted Hybrid RAG for Legal Contract Intelligence**

Turn lengthy legal PDFs into searchable, structured insights with semantic + keyword retrieval, knowledge-graph context, and Gemini-powered analysis.

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/UI-Streamlit-FF4B4B?logo=streamlit&logoColor=white)](https://streamlit.io/)
[![LLM-Gemini](https://img.shields.io/badge/LLM-Gemini%202.5%20Flash-8E75B2)](https://ai.google.dev/)
[![Retrieval-FAISS%20%2B%20BM25](https://img.shields.io/badge/Retrieval-FAISS%20%2B%20BM25-1877F2)](#-how-it-works)
[![Knowledge Graph-NetworkX](https://img.shields.io/badge/Knowledge%20Graph-NetworkX-138A55)](#-knowledge-graph)

</div>

---

## 🧭 Project at a glance

Legal-Ease AI is a Python and Streamlit application for exploring legal contracts. Upload a PDF, process its contents, review a generated summary and risk assessment, then ask questions and inspect the retrieved evidence used to form the answer.

It combines **Retrieval-Augmented Generation (RAG)** with **hybrid search** and a lightweight **legal knowledge graph** so that answers can draw on both relevant contract passages and extracted relationships.

> **Important:** Legal-Ease is an AI-assisted review tool, not a substitute for advice from a qualified legal professional. Summaries, extracted facts, and risk flags should be verified against the original contract.

## 🖼️ Architecture

The diagram below maps the main components and data flow—from PDF ingestion to a grounded answer and supporting contract references.

<div align="center">
  <img src="Legal-Ease%20AI%20Contract%20Analysis%20Architecture.png" alt="Legal-Ease AI end-to-end system architecture" width="100%">
  <p><em>End-to-end architecture: document processing, hybrid retrieval, graph context, LLM generation, and user-facing outputs.</em></p>
</div>

## ✨ What it can do

| Capability | What it does |
|---|---|
| 📄 **Contract ingestion** | Accepts a legal PDF and extracts text page by page. |
| 🧩 **Clause-aware chunking** | Splits content into smaller sections/chunks and retains useful document metadata. |
| 🔎 **Hybrid retrieval** | Combines FAISS semantic search with BM25 keyword search, then fuses the ranked results. |
| 🎯 **Re-ranking** | Uses a cross-encoder to prioritise passages that are more relevant to the question. |
| 🕸️ **Knowledge graph** | Extracts legal facts such as parties, obligations, clause types, and deadlines, and represents relationships as a graph. |
| 💬 **Contract Q&A** | Sends retrieved passages and available graph facts to Gemini to answer a natural-language question. |
| 📝 **Contract summary** | Produces an executive summary, parties, jurisdiction, key clauses, and important dates. |
| ⚠️ **Risk review** | Flags potential issues such as ambiguous terms, liability concerns, or missing clauses. |
| 📚 **Evidence inspection** | Shows retrieved contract chunks and graph facts in the UI so users can check the supporting context. |

## 🔄 How it works

### 1. Process the contract

1. **Upload a PDF** in the Streamlit sidebar and select **Process Contract**.
2. **Extract and parse text** page by page using the ingestion modules.
3. **Split the text into clause-aware chunks**, retaining information such as page, section, document name, and chunk type.
4. **Build retrieval indexes:** BGE embeddings are indexed with FAISS for semantic similarity, while BM25 supports keyword-oriented search.
5. **Create derived analysis:** Gemini generates a structured contract summary and risk assessment from the processed chunks.
6. **Build the graph:** the legal extractor identifies structured facts from a subset of chunks and the graph builder connects parties, obligations, clause types, and deadlines.

### 2. Ask a question

When a user submits a question, the app follows this path:

```text
User question
    │
    ▼
FAISS semantic search ──┐
                        ├──► Rank fusion ──► Cross-encoder re-ranking
BM25 keyword search ────┘                         │
                                                  ▼
                                      Retrieve graph context
                                                  │
                                                  ▼
                               Contract passages + graph facts
                                                  │
                                                  ▼
                                         Gemini 2.5 Flash
                                                  │
                                                  ▼
                             Answer + inspectable retrieved context
```

The interface displays the answer and, when available, graph facts and retrieved chunks. Retrieved document metadata is included in the prompt to support source-aware responses.

### 3. Explore the results

After processing, the UI presents four tabs:

- **Summary** — executive summary, contract type, jurisdiction, parties, key clauses, and important dates.
- **Risk Analysis** — an overall risk score and a list of potential issues with severity labels.
- **Chat** — ask questions about the contract, inspect graph facts used, and expand retrieved context.
- **Knowledge Graph** — inspect graph node and edge counts and a sample of the extracted relationships.

## 🔎 Why hybrid RAG?

Legal questions often use different wording from the contract itself. Each retrieval method contributes a different signal:

| Method | Strength | Example |
|---|---|---|
| **FAISS + BGE embeddings** | Finds semantically similar passages even when the wording differs. | “How can this agreement end?” may retrieve a termination clause. |
| **BM25 keyword retrieval** | Matches specific words and phrases. | “termination notice” can surface passages containing those terms. |
| **Rank fusion** | Combines the two ranked result lists rather than relying on only one search method. | A passage relevant by meaning or exact wording can enter the candidate set. |
| **Cross-encoder re-ranking** | Re-scores candidates against the actual user question. | More relevant passages are prioritised before answer generation. |
| **Knowledge-graph context** | Adds extracted relationships between entities, obligations, clause types, and deadlines when a query matches graph entities. | An obligation can be linked to a party and a deadline. |

This is **graph-assisted hybrid RAG**, not a full GraphRAG system: the current implementation builds a graph and retrieves direct neighbouring facts; broader graph-traversal retrieval and community-level reasoning remain future work.

## 🕸️ Knowledge graph

The graph is built using NetworkX. Extracted facts can connect:

- **Party** → obligation (relationship: `must`)
- **Obligation** → clause type (relationship: `belongs_to`)
- **Obligation** → deadline (relationship: `deadline`, when available)

Example:

```text
Employee ── must ──► Provide written notice
                            │
                            ├── belongs_to ──► Termination
                            │
                            └── deadline ────► 45 days
```

The graph offers a structured view of selected facts. Its coverage depends on what the extractor identifies and on the subset of chunks processed during graph construction.

## 🧰 Technology stack

| Area | Technologies |
|---|---|
| Language & UI | Python, Streamlit |
| LLM | Google Gemini 2.5 Flash |
| Embeddings | BAAI/bge-base-en-v1.5 |
| Semantic retrieval | FAISS |
| Keyword retrieval | BM25 |
| Re-ranking | `cross-encoder/ms-marco-MiniLM-L-6-v2` |
| Knowledge graph | NetworkX |
| PDF processing | PyMuPDF |
| LLM orchestration | LangChain |
| Data models | Pydantic |

## 🗂️ Codebase map

```text
.
├── app.py                         # Streamlit UI and end-to-end orchestration
├── requirements.txt               # Python dependencies
├── testing_chunking.py             # Chunking test script
└── src/
    ├── ingestion/
    │   ├── pdf_loader.py           # PDF text extraction
    │   ├── legal_parser.py         # Legal section parsing
    │   └── metadata_builder.py     # Document metadata helpers
    ├── chunking/
    │   ├── clause_chunker.py       # Clause-aware chunks
    │   ├── legal_chunk_model.py    # Chunk data model
    │   └── recursive_fallback.py   # Fallback chunk splitting
    ├── retrieval/
    │   ├── embedding_service.py    # BGE embedding service
    │   ├── faiss_store.py          # Vector index
    │   ├── bm25_store.py           # Keyword index
    │   ├── hybrid_retriever.py     # Rank fusion and retrieval
    │   └── reranker.py             # Cross-encoder re-ranking
    ├── legal_kg/
    │   ├── legal_extractor.py      # Structured legal fact extraction
    │   ├── kg_builder.py            # NetworkX graph construction
    │   └── kg_retriever.py          # Direct graph-neighbour context
    ├── llm/
    │   ├── legal_chain.py           # LLM setup
    │   └── legal_qa.py              # Prompted contract Q&A
    ├── summarization/
    │   ├── contract_summarizer.py  # Structured summaries
    │   ├── risk_analyzer.py         # Potential risk review
    │   └── summary_models.py        # Typed result models
    └── evaluation/
        ├── evaluator.py
        ├── evaluation_models.py
        └── metrics.py
```

## 🚀 Run locally

### Prerequisites

- Python 3.10 or newer
- A Google Gemini API key
- Git

### Setup

```bash
git clone https://github.com/Jayantsinghkhanna/-Legal-Ease-AI-.git
cd -Legal-Ease-AI-
python -m venv .venv
```

Activate the environment:

**Windows PowerShell**
```powershell
.venv\Scripts\Activate.ps1
```

**macOS / Linux**
```bash
source .venv/bin/activate
```

Install dependencies:

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

Set your Gemini API key as an environment variable before starting the app:

**Windows PowerShell**
```powershell
$env:GOOGLE_API_KEY="your_api_key_here"
```

**macOS / Linux**
```bash
export GOOGLE_API_KEY="your_api_key_here"
```

Run Streamlit:

```bash
streamlit run app.py
```

Open the local URL printed by Streamlit, upload a PDF, and select **Process Contract**.

> Keep API keys private. Do not hard-code secrets or commit them to Git.

## ⚙️ Configuration notes

- The **Top K Retrieval** slider controls the number of candidate passages requested for retrieval (3–20; default 10).
- The model and retrieval implementations are organised in separate modules under `src/`.
- The graph is built from the first 20 chunks in the current app workflow, so graph coverage may not include every clause in a long contract.
- Contract summaries and risk assessments also use a bounded subset of chunks in the current implementation; verify important findings against the complete source PDF.

## 🛣️ Potential next steps

- **Broader graph retrieval:** multi-hop traversal, entity linking, and relationship-aware candidate expansion.
- **Multi-document analysis:** compare contract versions and related agreements.
- **Evidence-first citations:** display source page and clause references directly beside each generated answer.
- **Evaluation suite:** measure retrieval relevance, answer faithfulness, and risk-flag quality on a curated test set.
- **Review workflow:** allow a reviewer to mark issues as valid, irrelevant, or requiring legal attention.

## 👤 Author

**Jayant Singh Khanna**  
Interested in Generative AI, RAG systems, knowledge graphs, and applied machine learning.

---

<div align="center">

**Legal-Ease AI** · Making complex contracts easier to explore and review.

*AI-assisted contract analysis. Always verify outputs against the original document.*

</div>
