import streamlit as st
import requests

st.title("AI 技术知识库 Agent 系统")

question = st.text_input("请输入问题")

if question:
    try:
        res = requests.post(
            "http://localhost:8000/chat",
            json={"question": question}
        )
        answer = res.json()["answer"]
        st.write("回答：")
        st.write(answer)
    except Exception as e:
        st.write(f"错误：{str(e)}")

st.write("\n示例问题：")
st.write("1. 什么是Transformer？")
st.write("2. 345*678是多少？")
st.write("3. 总结一下AI创业趋势")