import tempfile
import time

import streamlit as st

from src.ingestion.pdf_loader import (
    load_pdf
)

from src.ingestion.legal_parser import (
    extract_sections
)

from src.chunking.clause_chunker import (
    LegalClauseChunker
)

from src.retrieval.embedding_service import (
    EmbeddingService
)

from src.retrieval.faiss_store import (
    FAISSStore
)

from src.retrieval.bm25_store import (
    BM25Store
)

from src.retrieval.hybrid_retriever import (
    HybridRetriever
)

from src.retrieval.reranker import (
    LegalReranker
)

from src.llm.legal_chain import (
    LegalLLM
)

from src.llm.legal_qa import (
    LegalQA
)

from src.summarization.contract_summarizer import (
    ContractSummarizer
)

from src.summarization.risk_analyzer import (
    RiskAnalyzer
)

from src.legal_kg.legal_extractor import (
    LegalExtractor
)

from src.legal_kg.kg_builder import (
    LegalKGBuilder
)

from src.legal_kg.kg_retriever import (
    LegalKGRetriever
)


st.set_page_config(
    page_title="Legal-Ease AI",
    page_icon="⚖️",
    layout="wide"
)

st.title("⚖️ Legal-Ease AI")
st.caption(
    "Advanced Legal Contract Analysis using Hybrid RAG + Knowledge Graphs"
)

# ------------------------------------------------
# SIDEBAR
# ------------------------------------------------

with st.sidebar:

    st.header("Configuration")

    uploaded_file = st.file_uploader(
        "Upload Legal PDF",
        type=["pdf"]
    )

    top_k = st.slider(
        "Top K Retrieval",
        3,
        20,
        10
    )

    process_btn = st.button(
        "Process Contract"
    )

# ------------------------------------------------
# PROCESS DOCUMENT
# ------------------------------------------------

if uploaded_file and process_btn:

    with st.spinner(
        "Processing Contract..."
    ):

        start_time = time.time()

        with tempfile.NamedTemporaryFile(
            delete=False,
            suffix=".pdf"
        ) as tmp:

            tmp.write(
                uploaded_file.read()
            )

            pdf_path = tmp.name

        pages = load_pdf(
            pdf_path
        )

        chunker = (
            LegalClauseChunker()
        )

        chunks = []

        total_sections = 0

        for page in pages:

            sections = (
                extract_sections(
                    page["text"]
                )
            )

            total_sections += (
                len(sections)
            )

            page_chunks = (
                chunker.chunk_sections(
                    sections,
                    page["page_number"],
                    uploaded_file.name
                )
            )

            chunks.extend(
                page_chunks
            )

        # ---------------------------------------
        # VECTOR STORE
        # ---------------------------------------

        embeddings = (
            EmbeddingService()
            .get_embeddings()
        )

        vectorstore = (
            FAISSStore(
                embeddings
            )
            .create_index(
                chunks
            )
        )

        bm25_store = (
            BM25Store(
                chunks
            )
        )

        hybrid_retriever = (
            HybridRetriever(
                vectorstore,
                bm25_store
            )
        )

        reranker = (
            LegalReranker()
        )

        # ---------------------------------------
        # LLM
        # ---------------------------------------

        llm = (
            LegalLLM()
            .get_llm()
        )

        qa_system = (
            LegalQA(
                llm
            )
        )

        # ---------------------------------------
        # SUMMARY
        # ---------------------------------------

        summarizer = (
            ContractSummarizer()
        )

        summary = (
            summarizer.summarize(
                chunks
            )
        )

        risk_report = (
            RiskAnalyzer()
            .analyze(
                chunks
            )
        )

        # ---------------------------------------
        # KNOWLEDGE GRAPH
        # ---------------------------------------

        extractor = (
            LegalExtractor()
        )

        kg_builder = (
            LegalKGBuilder()
        )

        for chunk in chunks[:20]:

            try:

                knowledge = (
                    extractor.extract(
                        chunk.content
                    )
                )

                kg_builder.add_knowledge(
                    knowledge
                )

            except:
                pass

        graph = (
            kg_builder.graph
        )

        graph_retriever = (
            LegalKGRetriever(
                graph
            )
        )

        # Save Graph Retriever
        st.session_state[
            "graph_retriever"
        ] = graph_retriever

        st.session_state[
            "qa"
        ] = qa_system

        st.session_state[
            "retriever"
        ] = hybrid_retriever

        st.session_state[
            "reranker"
        ] = reranker

        st.session_state[
            "summary"
        ] = summary

        st.session_state[
            "risk"
        ] = risk_report

        st.session_state[
            "graph"
        ] = graph

        st.session_state[
            "chunks"
        ] = chunks

        st.session_state[
            "pages"
        ] = pages

        st.session_state[
            "sections"
        ] = total_sections

        st.session_state[
            "processing_time"
        ] = round(
            time.time()
            - start_time,
            2
        )

# ------------------------------------------------
# MAIN UI
# ------------------------------------------------

if "summary" in st.session_state:

    graph = st.session_state[
        "graph"
    ]

    st.subheader(
        "Contract Statistics"
    )

    c1, c2, c3, c4, c5 = st.columns(5)

    c1.metric(
        "Pages",
        len(
            st.session_state[
                "pages"
            ]
        )
    )

    c2.metric(
        "Sections",
        st.session_state[
            "sections"
        ]
    )

    c3.metric(
        "Chunks",
        len(
            st.session_state[
                "chunks"
            ]
        )
    )

    c4.metric(
        "Graph Nodes",
        graph.number_of_nodes()
    )

    c5.metric(
        "Graph Edges",
        graph.number_of_edges()
    )

    tab1, tab2, tab3, tab4 = st.tabs(
        [
            "Summary",
            "Risk Analysis",
            "Chat",
            "Knowledge Graph"
        ]
    )

    # ----------------------------------------
    # SUMMARY
    # ----------------------------------------

    with tab1:

        summary = st.session_state[
            "summary"
        ]

        st.subheader(
            "Executive Summary"
        )

        st.write(
            summary.executive_summary
        )

        st.markdown(
            f"**Contract Type:** {summary.contract_type}"
        )

        st.markdown(
            f"**Jurisdiction:** {summary.jurisdiction}"
        )

        st.markdown(
            "### Parties"
        )

        for party in summary.parties:

            st.write(
                f"• {party}"
            )

        st.markdown(
            "### Key Clauses"
        )

        for clause in summary.key_clauses:

            st.info(
                f"**{clause.clause_name}**\n\n{clause.summary}"
            )

        st.markdown(
            "### Important Dates"
        )

        for d in summary.important_dates:

            st.write(
                f"• {d.event}: {d.date}"
            )

    # ----------------------------------------
    # RISK
    # ----------------------------------------

    with tab2:

        risk = st.session_state[
            "risk"
        ]

        st.metric(
            "Risk Score",
            risk.risk_score
        )

        for item in risk.risks:

            st.warning(
                f"[{item.severity}] {item.issue}"
            )


    with tab3:

        st.subheader(
            "Ask Questions About Contract"
        )

        query = st.text_input(
            "Ask a legal question"
        )

        if st.button(
            "Get Answer"
        ):

            retriever = st.session_state[
                "retriever"
            ]

            reranker = st.session_state[
                "reranker"
            ]

            qa = st.session_state[
                "qa"
            ]

            graph_retriever = st.session_state[
                "graph_retriever"
            ]

            with st.spinner(
                "Analyzing Contract..."
            ):

                # -------------------------
                # Retrieval
                # -------------------------

                docs = retriever.retrieve(
                    query,
                    top_k
                )

                docs = reranker.rerank(
                    query,
                    docs
                )

                # -------------------------
                # Graph Context
                # -------------------------

                graph_context = []

                query_words = (
                    query.lower()
                    .replace("?", "")
                    .split()
                )

                for word in query_words:

                    try:

                        graph_context.extend(
                            graph_retriever.retrieve_context(
                                word
                            )
                        )

                    except:
                        pass

                graph_context = list(
                    set(graph_context)
                )

                # -------------------------
                # Generate Answer
                # -------------------------

                answer = qa.answer_question(
                    question=query,
                    documents=docs,
                    graph_context=graph_context
                )

                st.markdown(
                    "### Answer"
                )

                st.write(
                    answer
                )

                # -------------------------
                # Graph Facts
                # -------------------------

                if graph_context:

                    with st.expander(
                        "Knowledge Graph Facts Used"
                    ):

                        for fact in graph_context:

                            st.write(
                                f"• {fact}"
                            )

                # -------------------------
                # Retrieved Chunks
                # -------------------------

                with st.expander(
                    "Retrieved Context"
                ):

                    for i, doc in enumerate(
                        docs,
                        start=1
                    ):

                        st.markdown(
                            f"### Chunk {i}"
                        )

                        st.write(
                            doc.page_content[:1000]
                        )

                        st.divider()           

   

    # ----------------------------------------
    # GRAPH
    # ----------------------------------------

    with tab4:

        st.metric(
            "Nodes",
            graph.number_of_nodes()
        )

        st.metric(
            "Edges",
            graph.number_of_edges()
        )

        st.write(
            list(graph.nodes())[:50]
        )

        st.write(
            list(graph.edges())[:50]
        )

else:

    st.info(
        "Upload a contract and click Process Contract."
    )