import sys
import os

# 添加项目根目录到Python路径
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from rag.pipeline import RAGPipeline

class Tools:
    def __init__(self):
        self.rag_pipeline = RAGPipeline()
    
    def calculator(self, expr):
        try:
            # 提取表达式中的数字和运算符
            # 简单处理，只支持基本运算
            # 注意：实际应用中应该使用更安全的计算方法
            
            # 尝试直接计算
            try:
                result = eval(expr)
                return f"计算结果：{result}"
            except:
                # 如果直接计算失败，尝试提取表达式
                import re
                # 提取数字和运算符
                match = re.search(r'[\d\+\-\*\/\(\)\.]+', expr)
                if match:
                    expression = match.group()
                    result = eval(expression)
                    return f"计算结果：{result}"
                else:
                    return "无法识别的计算表达式"
        except Exception as e:
            return f"计算错误：{str(e)}"
    
    def search_tool(self, query):
        return self.rag_pipeline.run(query)