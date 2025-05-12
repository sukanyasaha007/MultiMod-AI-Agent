import chromadb

class VectorStore:
    def __init__(self):
        self.chroma = chromadb.Client()
        self.collection = self.chroma.create_collection("multimodal")

    def add_embeddings(self, ids, embeddings, metadata):
        self.collection.add(ids=ids, embeddings=embeddings, metadatas=metadata)

    def query(self, query_embedding, top_k=3):
        return self.collection.query(query_embeddings=[query_embedding], n_results=top_k)
