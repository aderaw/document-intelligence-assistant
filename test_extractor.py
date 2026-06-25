from pdf_reader import extract_text
from extractor import extract_info

file_path = "sample_docs/invoice.pdf"

text = extract_text(file_path)

result = extract_info(text)

print(result)