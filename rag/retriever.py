import os
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

class Retriever:
    def __init__(self, data_dir="data/raw", chunk_size=300, model_name="all-MiniLM-L6-v2"):
        self.data_dir = data_dir
        self.chunk_size = chunk_size
        self.embedding_model = SentenceTransformer(model_name)
        self.index = None
        self.chunks = []
        self._build_index()
    
    def _split_text(self, text):
        chunks = []
        for i in range(0, len(text), self.chunk_size):
            chunks.append(text[i:i+self.chunk_size])
        return chunks
    
    def _build_index(self):
        # 加载文档并切分
        for filename in os.listdir(self.data_dir):
            if filename.endswith(".md"):
                with open(os.path.join(self.data_dir, filename), "r", encoding="utf-8") as f:
                    text = f.read()
                    chunks = self._split_text(text)
                    self.chunks.extend(chunks)
        
        # 生成嵌入
        embeddings = self.embedding_model.encode(self.chunks)
        
        # 构建FAISS索引
        dimension = embeddings.shape[1]
        self.index = faiss.IndexFlatL2(dimension)
        self.index.add(np.array(embeddings))
    
    def search(self, query, k=3):
        # 生成查询嵌入
        query_embedding = self.embedding_model.encode([query])
        
        # 搜索最相似的文档
        D, I = self.index.search(query_embedding, k)
        
        # 返回检索到的文档
        retrieved_docs = [self.chunks[i] for i in I[0]]
        return "\n".join(retrieved_docs)

if __name__ == "__main__":
    retriever = Retriever()
    query = "什么是Transformer？"
    print(retriever.search(query))