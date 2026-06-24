import json

from langchain_google_genai import ChatGoogleGenerativeAI

from src.summarization.summary_models import (
    RiskAssessment
)


class RiskAnalyzer:

    def __init__(self):

        self.llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0
)

    def analyze(
        self,
        chunks
    ) -> RiskAssessment:

        context = "\n\n".join(
            [
                chunk.content
                for chunk in chunks[:20]
            ]
        )

        prompt = f"""
You are a senior legal contract reviewer.

Review this contract carefully.

Analyze the following areas:

1. Termination Clause
2. Liability Clause
3. Indemnification Clause
4. Confidentiality Clause
5. Payment Obligations
6. Jurisdiction / Governing Law
7. Force Majeure
8. Arbitration / Dispute Resolution

Identify:

- Missing clauses
- Unbalanced obligations
- Unlimited liability
- Ambiguous language
- Compliance concerns
- Potential legal risks

Return ONLY valid JSON.

Schema:

{{
    "risk_score": 0,
    "risks": [
        {{
            "severity": "Low | Medium | High",
            "issue": ""
        }}
    ]
}}

Risk Score Rules:

0-3 = Low Risk
4-6 = Medium Risk
7-10 = High Risk

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

        return RiskAssessment(
            **data
        )