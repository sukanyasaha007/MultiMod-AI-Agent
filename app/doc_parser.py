import fitz  # PyMuPDF
from sentence_transformers import SentenceTransformer

class DocParser:
    def __init__(self):
        self.embedder = SentenceTransformer("all-MiniLM-L6-v2")

    def extract_text(self, file_path):
        doc = fitz.open(file_path)
        text = " ".join(page.get_text() for page in doc)
        return text

    def embed_text(self, text):
        chunks = [text[i:i+500] for i in range(0, len(text), 500)]
        embeddings = self.embedder.encode(chunks)
        return chunks, embeddings
