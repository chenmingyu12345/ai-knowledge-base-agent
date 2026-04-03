import streamlit as st
import requests
import socket
import time

st.title("AI 技术知识库 Agent 系统")

# 测试API连接
st.sidebar.title("连接测试")
if st.sidebar.button("测试API连接"):
    try:
        st.sidebar.write("正在测试API连接...")
        # 测试端口是否开放
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex(('127.0.0.1', 8000))
        if result == 0:
            st.sidebar.write("✅ 端口 8000 开放")
            # 测试API服务
            res = requests.post(
                "http://127.0.0.1:8000/chat",
                json={"question": "测试连接"}
            )
            st.sidebar.write(f"✅ API响应状态码：{res.status_code}")
            st.sidebar.write("✅ API连接成功！")
        else:
            st.sidebar.write("❌ 端口 8000 未开放，API服务可能未启动")
    except Exception as e:
        st.sidebar.write(f"❌ 连接错误：{str(e)}")

question = st.text_input("请输入问题")

if question:
    st.write(f"您的问题：{question}")
    try:
        # 直接调用Agent来获取回答，绕过API服务
        import sys
        import os
        sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        from agent.agent import Agent
        
        st.write("正在处理...")
        agent = Agent()
        answer = agent.run(question)
        st.write("回答：")
        st.write(answer)
    except Exception as e:
        st.write(f"错误：{str(e)}")
        import traceback
        st.write(f"错误详情：{traceback.format_exc()}")

st.write("\n示例问题：")
st.write("1. 什么是Transformer？")
st.write("2. 345*678是多少？")
st.write("3. 总结一下AI创业趋势")