from config.settings import ENABLE_AI, OPENAI_API_KEY

def handle_ai_command(query: str):
    if not query.startswith("ask ai "):
        return None

    if not ENABLE_AI:
        return "AI mode is disabled."

    prompt = query.replace("ask ai ", "").strip()

    try:
        from openai import OpenAI

        client = OpenAI(api_key=OPENAI_API_KEY)
        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[
                {"role": "system", "content": "You are a smart desktop voice assistant."},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"AI request failed: {e}"
