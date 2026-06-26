import os
from dotenv import load_dotenv
from google import genai
from rag import SimpleRAG

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

rag = SimpleRAG()


def ask_pdf(text, question):
    rag.build_index(text)

    context_chunks = rag.retrieve(question)

    context = "\n\n".join(context_chunks)

    prompt = f"""
You are a helpful assistant.

Use ONLY the context below to answer the question.

Context:
{context}

Question:
{question}

Answer clearly and concisely.
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text