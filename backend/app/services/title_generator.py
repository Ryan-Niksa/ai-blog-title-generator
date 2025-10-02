from openai import OpenAI
from ..config import settings

def generate_titles(topic: str, n: int = 5) -> list[str]:
    """
    Generate blog title suggestions from a given topic using OpenAI.
    """
    if not settings.OPENAI_API_KEY:
        return [f"[Error] Missing OPENAI_API_KEY. Topic was: {topic}"]

    client = OpenAI(api_key=settings.OPENAI_API_KEY)

    try:
        prompt = (
            f"Suggest {n} catchy and engaging blog titles for the topic:\n\n"
            f"Topic: {topic}\n\n"
            f"Rules:\n"
            f"- Each title should be unique.\n"
            f"- Make them clear and engaging for a blog audience.\n"
            f"- Keep under 60 characters if possible."
        )

        resp = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
        )

        text = resp.choices[0].message.content.strip()
        titles = [line.lstrip("0123456789.-) ").strip() for line in text.split("\n") if line.strip()]
        return titles[:n]

    except Exception as e:
        return [f"[OpenAI error: {e}]"]
