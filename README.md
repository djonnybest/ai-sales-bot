# ИИ-продажник — тестовое задание

## Структура проекта по шагам

```
chatbot/
├── step1_salesbot/
│   ├── bot.py                # Streamlit-бот (основная рабочая версия)
│   ├── crm_data.json         # Эмулированные CRM-данные
│   └── requirements.txt      # Зависимости для запуска
│
├── step2_call_analysis/
│   └── call_analysis.md      # Анализ звонка, ошибки/успехи, рекомендации
│
├── step3_sales_script/
│   └── sales_script.md       # Шаблон скрипта продаж, структура, триггеры
│
├── step4_reels_automation/
│   ├── reels_automation.md   # Концепция автоматизации Reels через ИИ
│   └── reels_automation_code.py # Примеры кода для автоматизации этапов
│
└── README.md                # Инструкция и описание структуры
```

## Как запускать

### Шаг 1: ИИ-продажник (чат-бот)
1. Перейдите в папку `step1_salesbot`.
2. Установите зависимости:
   ```
   pip install -r requirements.txt
   ```
3. Запустите:
   ```
   streamlit run bot.py
   ```
4. Откройте браузер: http://localhost:8501

### Шаги 2–4
- Откройте соответствующие `.md`-файлы для анализа, скрипта и концепции.
- В `step4_reels_automation/reels_automation_code.py` — примеры кода для автоматизации.

---

## Для деплоя на GitHub
- Загрузите всю папку `chatbot` с сохранённой структурой.
- В каждом шаге только нужные файлы, лишнее удалено.

---

**Вопросы — пишите!**

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