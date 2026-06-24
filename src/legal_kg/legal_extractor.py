import json

from langchain_google_genai import (
    ChatGoogleGenerativeAI
)

from src.legal_kg.schemas import (
    LegalKnowledge
)


class LegalExtractor:

    def __init__(self):

        self.llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0
)

    def extract(
        self,
        text
    ):

        prompt = f"""
You are an expert legal contract analyst.

Extract:

1. Parties
2. Obligations
3. Deadlines
4. Clause Types

Return ONLY valid JSON.

Schema:

{{
    "facts":[
        {{
            "party":"",
            "obligation":"",
            "clause_type":"",
            "deadline":""
        }}
    ]
}}

Text:

{text}
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

        try:

            data = json.loads(
                cleaned
            )

            return LegalKnowledge(
                **data
            )

        except Exception:

            return LegalKnowledge(
                facts=[]
            )