
from app.image_processor import ImageProcessor
from app.doc_parser import DocParser
from app.vector_store import VectorStore
from langchain.llms import OpenAI

class MultiModalAgent:
    def __init__(self):
        self.img_proc = ImageProcessor()
        self.doc_proc = DocParser()
        self.vector_store = VectorStore()
        self.llm = OpenAI(temperature=0)

    def ingest(self, image_path, doc_path):
        # Process and embed image
        img_embedding = self.img_proc.embed_image(image_path)
        self.vector_store.add_embeddings(
            ids=["image1"],
            embeddings=[img_embedding],
            metadata=[{"type": "image", "path": image_path}]
        )

        # Process and embed document
        text = self.doc_proc.extract_text(doc_path)
        chunks, embeddings = self.doc_proc.embed_text(text)
        for i, (chunk, emb) in enumerate(zip(chunks, embeddings)):
            self.vector_store.add_embeddings(
                ids=[f"doc_chunk_{i}"],
                embeddings=[emb],
                metadata=[{"type": "text", "content": chunk}]
            )

    def answer_question(self, question):
        # (For now we skip re-embedding question; placeholder logic)
        context = "Simulated RAG context from top matches..."
        prompt = f"Question: {question}\nContext: {context}\nAnswer:"
        return self.llm(prompt)
