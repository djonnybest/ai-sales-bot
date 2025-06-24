import streamlit as st
import json
import openai
from streamlit_chat import message

# OpenAI API ключ теперь читается из секретов Streamlit
openai.api_key = st.secrets["OPENAI_API_KEY"]

with open('chatbot/crm_data.json', 'r', encoding='utf-8') as f:
    crm_data = json.load(f)

client_names = [client["client_name"] for client in crm_data]

st.set_page_config(page_title="ИИ-продажник — чат", page_icon="🤖")
st.title("🤖 ИИ-продажник — чат-демо")

if "client" not in st.session_state:
    st.session_state.client = client_names[0]
if "history" not in st.session_state:
    st.session_state.history = []

st.sidebar.header("CRM")
st.session_state.client = st.sidebar.selectbox("Выберите клиента:", client_names, index=client_names.index(st.session_state.client))
client_info = next(c for c in crm_data if c["client_name"] == st.session_state.client)
st.sidebar.write(client_info)

st.markdown("---")

for i, (user, bot) in enumerate(st.session_state.history):
    message(user, is_user=True, key=f"user_{i}")
    message(bot, is_user=False, key=f"bot_{i}")

user_input = st.text_input("Ваш запрос", key="input")

if st.button("Отправить") or (user_input and st.session_state.get("last_input") != user_input):
    if user_input:
        st.session_state["last_input"] = user_input
        prompt = f"""
        Клиент: {client_info['client_name']}
        Предыдущая покупка: {client_info['last_purchase']}
        Бюджет: {client_info['budget']} руб.
        Статус сделки: {client_info['deal_status']}
        Запрос клиента: {user_input}
        ---
        Ты — опытный продажник премиум-авто. Ответь клиенту, предложи релевантное решение или upsell, учитывая его бюджет, статус сделки и историю покупок. Будь вежлив, пиши на русском.
        """
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Ты — опытный продажник премиум-авто."},
                {"role": "user", "content": prompt}
            ]
        )
        answer = response['choices'][0]['message']['content']
        st.session_state.history.append((user_input, answer))
        st.experimental_rerun()

if st.button("Очистить диалог"):
    st.session_state.history = []
    st.session_state["last_input"] = ""
    st.experimental_rerun() 