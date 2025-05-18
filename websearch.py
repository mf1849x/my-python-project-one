from openai import OpenAI
client = OpenAI()

response = client.responses.create(
    model="gpt-4o-mini",
    tools=[{"type": "web_search_preview"}],
    input="Tell me about ai agents"
)

print(response.output_text)