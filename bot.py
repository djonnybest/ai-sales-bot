import streamlit as st
import json
import openai

# Загрузка CRM-данных
with open('crm_data.json', 'r', encoding='utf-8') as f:
    crm_data = json.load(f)

# Настройки OpenAI (замените на свой ключ)
openai.api_key = st.secrets["OPENAI_API_KEY"] if "OPENAI_API_KEY" in st.secrets else "sk-..."

st.title("🤖 ИИ-продажник — демо")

# Выбор клиента
client_names = [client["client_name"] for client in crm_data]
selected_client = st.selectbox("Выберите клиента:", client_names)
client_info = next(c for c in crm_data if c["client_name"] == selected_client)

st.write(f"**CRM:** {client_info}")

# Ввод запроса клиента
user_input = st.text_input("Запрос клиента (например, 'Хочу Bentley'):")

if user_input:
    # Формируем промпт для GPT
    prompt = f"""
    Клиент: {client_info['client_name']}
    Предыдущая покупка: {client_info['last_purchase']}
    Бюджет: {client_info['budget']} руб.
    Статус сделки: {client_info['deal_status']}
    Запрос клиента: {user_input}
    ---
    Ты — опытный продажник премиум-авто. Ответь клиенту, предложи релевантное решение или upsell, учитывая его бюджет, статус сделки и историю покупок. Будь вежлив, пиши на русском.
    """
    
    # Запрос к OpenAI
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "system", "content": "Ты — опытный продажник премиум-авто."},
                 {"role": "user", "content": prompt}]
    )
    st.markdown(f"**ИИ-продажник:** {response['choices'][0]['message']['content']}") 