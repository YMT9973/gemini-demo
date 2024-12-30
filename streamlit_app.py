import streamlit as st
import google.generativeai as genai
import env as env

# タイトルと説明
st.title("💬 Gemini Chatbot")
st.caption("🚀 Geminiを使ったChatbotになってます。API自身はインターネットに接続してません。")

# Gemini APIのAPIキー設定
genai.configure(api_key=env.gemini_api_key)

# Geminiモデルの定義
model = genai.GenerativeModel('gemini-1.0-pro-001')

# セッションにメッセージがない場合は初期化
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]

# 既存のメッセージを表示
for msg in st.session_state.messages:
    # シンプルなテキスト表示を使用
    st.text(f"{msg['role']}: {msg['content']}")

# ユーザー入力の取得
prompt = st.text_input("Your message:")

if prompt:
    # ユーザー入力をセッションに追加
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Gemini APIを使って応答を生成
    response = model.generate_content(prompt)

    # 応答をテキストとして取得
    assistant_response = response.text

    # 応答をセッション状態に追加し、表示
    st.session_state.messages.append({"role": "assistant", "content": assistant_response})
    st.text(f"Assistant: {assistant_response}")
