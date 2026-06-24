import json

from langchain_google_genai import ChatGoogleGenerativeAI

from src.summarization.summary_models import (
    ContractSummary
)


class ContractSummarizer:

    def __init__(self):

        self.llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0
)

    def summarize(
        self,
        chunks
    ) -> ContractSummary:

        context = "\n\n".join(
            [
                chunk.content
                for chunk in chunks[:20]
            ]
        )

        prompt = f"""
You are a legal contract analyst.

Analyze this legal contract.

Extract:

1. Contract Type
2. Parties
3. Governing Law / Jurisdiction
4. Executive Summary
5. Key Clauses
6. Important Dates
7. Major Obligations

Return ONLY valid JSON.

Required schema:

{{
    "contract_type":"",
    "parties":[],
    "jurisdiction":"",
    "executive_summary":"",
    "key_clauses":[
        {{
            "clause_name":"",
            "summary":""
        }}
    ],
    "important_dates":[
        {{
            "event":"",
            "date":""
        }}
    ]
}}

Contract:

{context}
"""

        response = self.llm.invoke(
            prompt
        )

        cleaned = (
            response.content
            .replace("```json", "")
            .replace("```", "")
            .strip()
        )

        data = json.loads(cleaned)

        return ContractSummary(
            **data
        )