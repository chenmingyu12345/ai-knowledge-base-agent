import sys
import os

# 添加项目根目录到Python路径
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from tools.tools import Tools
from model.model_loader import LLM

class Agent:
    def __init__(self):
        self.tools = Tools()
        self.llm = LLM()
    
    def run(self, question):
        # 简单的任务规划逻辑
        if any(keyword in question for keyword in ["多少", "*", "+", "-", "/", "计算", "等于"]):
            return self.tools.calculator(question)
        elif any(keyword in question for keyword in ["什么是", "定义", "原理", "如何", "怎样"]):
            return self.tools.search_tool(question)
        else:
            # 直接使用LLM回答
            return self.llm.generate(question)

if __name__ == "__main__":
    agent = Agent()
    # 测试技术问题
    print("测试技术问题：")
    print(agent.run("什么是Transformer？"))
    print("\n测试计算问题：")
    print(agent.run("345*678是多少？"))
    print("\n测试简单问题：")
    print(agent.run("总结一下AI创业趋势"))