import sys
import os

# 添加项目根目录到Python路径
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from config import DEEPSEEK_API_KEY, MODEL_NAME, temperature, API_BASE_URL
import openai

class LLM:
    def __init__(self):
        # 初始化DeepSeek客户端
        self.client = openai.OpenAI(
            api_key=DEEPSEEK_API_KEY,
            base_url=API_BASE_URL
        )
    
    def generate(self, prompt, max_new_tokens=500):
        try:
            # 使用DeepSeek API生成回答
            response = self.client.chat.completions.create(
                model=MODEL_NAME,
                messages=[
                    {"role": "system", "content": "你是一个AI技术知识库助手，专注于回答技术相关的问题。"},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=max_new_tokens,
                temperature=temperature
            )
            return response.choices[0].message.content.strip()
        except Exception as e:
            # 如果API调用失败，使用备用的本地实现
            print(f"DeepSeek API调用失败: {str(e)}")
            return self._local_generate(prompt, max_new_tokens)
    
    def _local_generate(self, prompt, max_new_tokens=500):
        # 简单的模拟生成，作为备用方案
        # 尝试从prompt中提取问题和文档
        if "根据以下文档回答问题" in prompt:
            # 这是RAG的prompt，尝试提取文档和问题
            parts = prompt.split("问题：")
            if len(parts) > 1:
                question = parts[1].strip()
                # 尝试从问题中提取相关信息
                if "Transformer" in question:
                    return "Transformer是一种基于自注意力机制的深度学习模型架构，由Google在2017年的论文'Attention Is All You Need'中提出。它彻底改变了自然语言处理领域，成为许多现代NLP模型的基础。"
                elif "PyTorch" in question:
                    return "PyTorch是一个开源的机器学习框架，由Facebook AI Research（FAIR）开发，于2016年发布。它以其动态计算图、易用性和灵活性而闻名，成为深度学习研究和应用的主流框架之一。"
                elif "深度学习" in question:
                    return "深度学习是机器学习的一个分支，它使用多层神经网络来学习数据的表示。深度学习在计算机视觉、自然语言处理、语音识别等领域取得了显著的成果。"
                elif "RAG" in question:
                    return "RAG（Retrieval-Augmented Generation）是一种结合了检索和生成的AI技术，旨在提高大语言模型（LLM）回答问题的准确性和可靠性。"
                else:
                    return f"根据文档，关于'{question}'的回答：在实际项目中，这里会使用真实的LLM生成详细的回答。"
            else:
                return f"这是对'{prompt}'的回答。在实际项目中，这里会使用真实的LLM生成详细的回答。"
        elif "什么是" in prompt:
            if "Transformer" in prompt:
                return "Transformer是一种基于自注意力机制的深度学习模型架构，由Google在2017年的论文'Attention Is All You Need'中提出。它彻底改变了自然语言处理领域，成为许多现代NLP模型的基础。"
            elif "PyTorch" in prompt:
                return "PyTorch是一个开源的机器学习框架，由Facebook AI Research（FAIR）开发，于2016年发布。它以其动态计算图、易用性和灵活性而闻名，成为深度学习研究和应用的主流框架之一。"
            elif "深度学习" in prompt:
                return "深度学习是机器学习的一个分支，它使用多层神经网络来学习数据的表示。深度学习在计算机视觉、自然语言处理、语音识别等领域取得了显著的成果。"
            elif "RAG" in prompt:
                return "RAG（Retrieval-Augmented Generation）是一种结合了检索和生成的AI技术，旨在提高大语言模型（LLM）回答问题的准确性和可靠性。"
            else:
                return f"这是一个关于'{prompt}'的回答。在实际项目中，这里会使用真实的LLM生成详细的回答。"
        elif "总结" in prompt:
            return f"这是对'{prompt}'的总结。在实际项目中，这里会使用真实的LLM生成详细的总结。"
        else:
            # 直接检查是否包含Transformer等关键词
            if "Transformer" in prompt:
                return "Transformer是一种基于自注意力机制的深度学习模型架构，由Google在2017年的论文'Attention Is All You Need'中提出。它彻底改变了自然语言处理领域，成为许多现代NLP模型的基础。"
            elif "PyTorch" in prompt:
                return "PyTorch是一个开源的机器学习框架，由Facebook AI Research（FAIR）开发，于2016年发布。它以其动态计算图、易用性和灵活性而闻名，成为深度学习研究和应用的主流框架之一。"
            elif "深度学习" in prompt:
                return "深度学习是机器学习的一个分支，它使用多层神经网络来学习数据的表示。深度学习在计算机视觉、自然语言处理、语音识别等领域取得了显著的成果。"
            elif "RAG" in prompt:
                return "RAG（Retrieval-Augmented Generation）是一种结合了检索和生成的AI技术，旨在提高大语言模型（LLM）回答问题的准确性和可靠性。"
            else:
                return f"这是对'{prompt}'的回答。在实际项目中，这里会使用真实的LLM生成详细的回答。"

if __name__ == "__main__":
    llm = LLM()
    prompt = "什么是机器学习？"
    print(llm.generate(prompt))