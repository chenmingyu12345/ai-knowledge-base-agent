from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import sys
import os

# 添加项目根目录到Python路径
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from agent.agent import Agent

app = FastAPI()

class ChatRequest(BaseModel):
    question: str

@app.post("/chat")
def chat(request: ChatRequest):
    # 打印接收到的问题
    print(f"接收到的问题: {request.question}")
    
    agent = Agent()
    answer = agent.run(request.question)
    
    # 打印生成的回答
    print(f"生成的回答: {answer}")
    
    return JSONResponse(content={"answer": answer}, media_type="application/json; charset=utf-8")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)