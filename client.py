from openai import OpenAI
import time

# pip install openai
# if you saved the key under a different environment variable name, you can do something like:
client = OpenAI(api_key="Your_OpenAI_API_Key")

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a virtual assistant named JARVIS, skilled in coding."},
    {"role": "user", "content": "What is coding?"}
  ]
)

print(completion.choices[0].message)