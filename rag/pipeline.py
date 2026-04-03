import sys
import os

# 添加项目根目录到Python路径
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from rag.retriever import Retriever
from model.model_loader import LLM

class RAGPipeline:
    def __init__(self):
        self.retriever = Retriever()
        self.llm = LLM()
    
    def run(self, question):
        # 检索相关文档
        docs = self.retriever.search(question)
        
        # 构建提示
        prompt = f"根据以下文档回答问题：\n\n{docs}\n\n问题：{question}"
        
        # 生成回答
        answer = self.llm.generate(prompt)
        
        return answer

if __name__ == "__main__":
    pipeline = RAGPipeline()
    question = "什么是Transformer？"
    print(pipeline.run(question))