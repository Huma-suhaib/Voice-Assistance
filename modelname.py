from openai import OpenAI

client = OpenAI(
    api_key="Your_API"
)

completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant named Sofia like alexa and google cloud."},
        {
            "role": "user", "content": "What is love?"
        }
    ]
)
print(completion.choices[0].message)
