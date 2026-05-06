import streamlit as st
import os
import time

st.set_page_config(page_title="Local AI Assistant", page_icon="🤖")

DB_FILE = "chat_history.txt"

def save_to_file(role, content):
    with open(DB_FILE, "a", encoding="utf-8") as f:
        f.write(f"{role}|{content}\n")

def load_from_file():
    if not os.path.exists(DB_FILE): return []
    history = []
    with open(DB_FILE, "r", encoding="utf-8") as f:
        for line in f:
            if "|" in line:
                role, content = line.strip().split("|", 1)
                history.append({"role": role, "content": content})
    return history

def get_mock_response(user_text):
    user_text = user_text.lower().strip()
    
    if any(word in user_text for word in ["hi", "hello", "hey"]):
        return "Hi there! How can I help you today?"
    
    elif "how are you" in user_text:
        return "I am doing great, thank you! How about you?"
    
    elif "name" in user_text:
        return "I am your Local AI Assistant, created for the MSS task."
    
    elif "how" in user_text and "work" in user_text:
        return "I work locally using Python. No internet or APIs required!"
    
    elif "remember" in user_text or "refresh" in user_text:
        return "Yes! I save everything to a file, so I never forget our chat."
    
    elif "thank" in user_text:
        return "You are very welcome, Yasmeen! Good luck with your demo."

    else:
        return "That's cool! Ask me something else like 'What is your name?' or 'How do you work?'"

st.title("🤖 Local AI Assistant")
st.caption("🚀 Implementation for MSS Task | Created by Eng. Yasmeen")

with st.sidebar:
    if st.button("Clear History"):
        if os.path.exists(DB_FILE): os.remove(DB_FILE)
        st.rerun()

history = load_from_file()
for msg in history:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

if prompt := st.chat_input("Type your message..."):
    with st.chat_message("user"):
        st.markdown(prompt)
    save_to_file("user", prompt)

    with st.chat_message("assistant"):
        response = get_mock_response(prompt)
        placeholder = st.empty()
        full_res = ""
        for word in response.split():
            full_res += word + " "
            time.sleep(0.05)
            placeholder.markdown(full_res + "▌")
        placeholder.markdown(response)
    
    save_to_file("assistant", response)
    st.rerun()