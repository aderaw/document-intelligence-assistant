from pdf_reader import extract_text
from chat_rag import ask_pdf

file_path = "sample_docs/invoice.pdf"

with open(file_path, "rb") as f:
    text = extract_text(f)

question = "What is the total invoice amount?"

answer = ask_pdf(text, question)

print("\n🤖 AI ANSWER:\n")
print(answer)