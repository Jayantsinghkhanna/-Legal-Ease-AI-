from langchain_core.prompts import (
    ChatPromptTemplate
)


class LegalQA:

    def __init__(self, llm):

        self.llm = llm

    def answer_question(
    self,
    question,
    documents,
    graph_context=None
):

        context_parts = []

        for doc in documents:

            metadata = getattr(
                doc,
                "metadata",
                {}
            )

            document_name = metadata.get(
                "document_name",
                "Unknown Document"
            )

            page = metadata.get(
                "page",
                "Unknown Page"
            )

            section = metadata.get(
                "section",
                "Unknown Section"
            )

            content = getattr(
                doc,
                "page_content",
                ""
            )

            context_parts.append(
                f"""
DOCUMENT:
{document_name}

PAGE:
{page}

SECTION:
{section}

CONTENT:
{content}
"""
            )

        context = "\n\n".join(
            context_parts
        )
        graph_section = "\n".join(
    graph_context or []
)

        prompt = ChatPromptTemplate.from_template(
    """
You are Legal-Ease,
an expert legal contract assistant.

Use BOTH:

1. Graph Facts
2. Retrieved Legal Documents

STRICT RULES:

1. Use only supplied information.
2. Never hallucinate.
3. Cite sources.
4. Prefer graph facts if available.

GRAPH FACTS:

{graph_context}

DOCUMENT CONTEXT:

{context}

Question:

{question}
"""
)

        chain = prompt | self.llm

        response = chain.invoke(
            {
                "context": context,
                "question": question,
                "graph_context": graph_section  
            }
        )

        return response.content