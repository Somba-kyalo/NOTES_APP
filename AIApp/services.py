from openai import OpenAI
from django.conf import settings


client = OpenAI(
    api_key=settings.OPENROUTER_API_KEY,
    base_url="https://openrouter.ai/api/v1",
)


def generate_summary(content):
    response = client.chat.completions.create(
        model="openrouter/free",
        messages=[
            {
                "role": "user",
                "content": f"Summarize the following note clearly and concisely:\n\n{content}",
            }
        ],
    )

    return response.choices[0].message.content