# app/llm.py
import os
from groq import Groq
from app.prompts import DATATHON_EXTRACTION_PROMPT

def call_groq(text: str):
    api_key = os.getenv("GROQ_API_KEY")

    if not api_key:
        raise ValueError("❌ GROQ_API_KEY not found in environment!")

    client = Groq(api_key=api_key)

    prompt = DATATHON_EXTRACTION_PROMPT + "\n\nExtract from this invoice:\n" + text

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",     # ✅ works
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )

    return response.choices[0].message.content
