# ИИ-продажник — чат-бот на Streamlit

## Как запустить локально

1. Установите зависимости:
   ```
   pip install -r requirements.txt
   ```

2. Запустите приложение:
   ```
   streamlit run streamlit_chat.py
   ```

3. Откройте браузер по адресу http://localhost:8501

## Как задеплоить на Streamlit Community Cloud

1. Загрузите этот репозиторий на GitHub.
2. Перейдите на https://share.streamlit.io/ и выберите свой репозиторий.
3. Укажите путь к файлу: `streamlit_chat.py`
4. В разделе **Settings → Secrets** добавьте ваш OpenAI API ключ:
   ```
   OPENAI_API_KEY=sk-...
   ```
5. Нажмите "Deploy".

## Пример CRM-данных

Файл `crm_data.json` должен быть в корне проекта. Пример:
```json
[
  {
    "client_name": "Иван",
    "last_purchase": "Audi Q7",
    "budget": 15000000,
    "deal_status": "В переговорах"
  },
  {
    "client_name": "Мария",
    "last_purchase": "BMW X5",
    "budget": 7000000,
    "deal_status": "Новая заявка"
  },
  {
    "client_name": "Алексей",
    "last_purchase": "Kia Rio",
    "budget": 2000000,
    "deal_status": "Закрыта успешно"
  }
]
``` 