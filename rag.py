import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")


class SimpleRAG:
    def __init__(self):
        self.text_chunks = []
        self.index = None

    def chunk_text(self, text, chunk_size=500):
        words = text.split()
        return [" ".join(words[i:i+chunk_size]) for i in range(0, len(words), chunk_size)]

    def build_index(self, text):
        self.text_chunks = self.chunk_text(text)

        embeddings = model.encode(self.text_chunks)

        dim = embeddings.shape[1]
        self.index = faiss.IndexFlatL2(dim)
        self.index.add(np.array(embeddings))

    def retrieve(self, query, k=3):
        query_embedding = model.encode([query])

        distances, indices = self.index.search(np.array(query_embedding), k)

        return [self.text_chunks[i] for i in indices[0]]