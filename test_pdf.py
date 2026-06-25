from pdf_reader import extract_text

file_path = "sample_docs/invoice.pdf"

text = extract_text(file_path)

print(text[:2000])