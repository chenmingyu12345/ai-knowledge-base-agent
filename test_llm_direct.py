import sys
import os

# 添加项目根目录到Python路径
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from model.model_loader import LLM

print("测试LLM的DeepSeek API调用...")
print("=" * 60)

llm = LLM()

# 测试1: 简单的问题
print("\n测试1: 什么是机器学习？")
result1 = llm.generate("什么是机器学习？")
print(f"结果: {result1}")

# 测试2: 总结性问题
print("\n测试2: 总结一下AI创业趋势，以及一人公司是什么？")
result2 = llm.generate("总结一下AI创业趋势，以及一人公司是什么？")
print(f"结果: {result2}")

# 测试3: 简单问题
print("\n测试3: 你好")
result3 = llm.generate("你好")
print(f"结果: {result3}")

print("\n" + "=" * 60)
print("测试完成！")
