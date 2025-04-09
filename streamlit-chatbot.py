# import streamlit as st
# from transformers import pipeline
# from datetime import datetime

# @st.cache_resource
# def load_chatbot():
#     return pipeline("question-answering", model="distilbert-base-cased-distilled-squad")

# chatbot = load_chatbot()

# if "chat_history" not in st.session_state:
#     st.session_state.chat_history = []

# st.title("💬 AI Chatbot (Q&A Mode)")
# st.markdown("Menggunakan model `distilbert-base-cased-distilled-squad` dari Hugging Face 🤗")

# # Context chatbot (jawaban diambil dari sini)
# context = st.text_area("🧠 Masukkan konteks/topik utama chatbot:", 
#                        "Python adalah bahasa pemrograman yang populer untuk AI dan data science.")

# # Input pengguna
# user_input = st.text_input("Tanyakan sesuatu:")

# if st.button("Kirim"):
#     if user_input.strip():
#         st.session_state.chat_history.append({"sender": "You", "message": user_input, "time": datetime.now().strftime("%H:%M")})
#         result = chatbot(question=user_input, context=context)
#         answer = result['answer']
#         st.session_state.chat_history.append({"sender": "Bot", "message": answer, "time": datetime.now().strftime("%H:%M")})

# st.markdown("### 🗨️ Riwayat Percakapan")
# for chat in st.session_state.chat_history:
#     with st.chat_message(chat["sender"].lower()):
#         st.markdown(f"{chat['message']}  \n⌚ {chat['time']}")


import streamlit as st
from transformers import pipeline

# Setup pipeline with Hugging Face model (Flan-T5)
@st.cache_resource


def load_bot():
    return pipeline(
        "text2text-generation",
        model="google/flan-t5-small",  # atau flan-t5-base
        tokenizer="google/flan-t5-small",
        max_length=200,
    )

bot = load_bot()

# Chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

st.title("🧠 AI Chatbot Bubble Style")
st.markdown("Powered by `flan-t5-xl` from Hugging Face 🤗")

# Show chat bubbles
for chat in st.session_state.chat_history:
    with st.chat_message(chat["role"]):
        st.markdown(chat["content"])

# Input box di bawah
user_input = st.chat_input("Tulis pesan di sini...")

if user_input:
    # Tampilkan input user
    st.chat_message("user").markdown(user_input)
    st.session_state.chat_history.append({"role": "user", "content": user_input})

    # Dapatkan respons dari model
    with st.spinner("Mengetik..."):
        response = bot(f"Q: {user_input} A:")[0]['generated_text']
    
    # Tampilkan output
    st.chat_message("assistant").markdown(response)
    st.session_state.chat_history.append({"role": "assistant", "content": response})
