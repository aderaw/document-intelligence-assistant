from pdf_reader import extract_text
from rag import SimpleRAG

file_path = "sample_docs/invoice.pdf"

text = extract_text(open(file_path, "rb"))

rag = SimpleRAG()
rag.build_index(text)

query = "What is the total amount?"

results = rag.search(query)

for r in results:
    print("\n--- CHUNK ---\n")
    print(r)