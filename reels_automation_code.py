import openai
import requests
# from pytrends.request import TrendReq  # Раскомментируйте, если нужен Google Trends

# 1. Получение трендов (пример с Google Trends)
def get_trends(keyword="электромобили"):
    """
    Получить тренды по ключевому слову (пример с pytrends)
    """
    try:
        from pytrends.request import TrendReq
        pytrends = TrendReq(hl='ru-RU', tz=180)
        pytrends.build_payload([keyword], cat=0, timeframe='now 7-d', geo='RU')
        trends = pytrends.related_queries()
        return trends[keyword]['top'] if trends[keyword]['top'] is not None else []
    except Exception as e:
        return f"Ошибка получения трендов: {e}"

# 2. Генерация идеи и сценария для рилса через GPT
def generate_reel_idea(trend, openai_api_key):
    openai.api_key = openai_api_key
    prompt = f"""
    Ты — креативный SMM-менеджер. На основе тренда "{trend}" придумай идею для короткого рилса (Instagram/TikTok), опиши сценарий (3-5 шагов), предложи заголовок и 5 хэштегов.
    Ответ дай в формате:
    Идея:
    Сценарий:
    Заголовок:
    Хэштеги:
    """
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Ты — креативный SMM-менеджер."},
            {"role": "user", "content": prompt}
        ]
    )
    return response['choices'][0]['message']['content']

# 3. Генерация видео (заглушка для интеграции с AI-видеосервисом)
def generate_video(scenario_text):
    """
    Пример функции-заглушки для интеграции с Runway/Pika/Kaiber/HeyGen через API.
    В no/low code сервисах используйте HTTP-запрос к нужному сервису.
    """
    # Здесь должен быть код отправки запроса к AI-видеосервису
    # Например, requests.post('https://api.runwayml.com/v1/generate', ...)
    return f"[Видео сгенерировано по сценарию: {scenario_text[:50]}...]"

# 4. Публикация видео через Webhook (например, Zapier/Make)
def publish_video_via_webhook(title, description, video_url, webhook_url):
    data = {
        "title": title,
        "description": description,
        "video_url": video_url
    }
    response = requests.post(webhook_url, json=data)
    return response.status_code, response.text

# Пример использования (можно запускать поэтапно в no/low code сервисах):
if __name__ == "__main__":
    # 1. Получить тренды
    # trends = get_trends("электромобили")
    # print(trends)

    # 2. Сгенерировать идею и сценарий
    trend = "электромобили в России"
    openai_api_key = "sk-..."  # Замените на свой ключ
    idea = generate_reel_idea(trend, openai_api_key)
    print("\n=== Идея и сценарий ===\n", idea)

    # 3. Сгенерировать видео (заглушка)
    video_url = generate_video(idea)
    print("\n=== Видео ===\n", video_url)

    # 4. Опубликовать через webhook (пример)
    # webhook_url = "https://hooks.zapier.com/hooks/catch/ВАШ_ЗАП_ИД/ВАШ_КЛЮЧ/"
    # status, resp = publish_video_via_webhook("Трендовый рилс", idea, video_url, webhook_url)
    # print(f"Webhook status: {status}, response: {resp}") 