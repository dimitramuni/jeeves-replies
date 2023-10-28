
import os
import openai
openai.api_key_path ='/Users/muni/Desktop/secret_key.py'

completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex mathematical concepts with creative flair."},
    {"role": "user", "content": "Compose a sonnet that explains the concept of integration."}
  ]
)

print(completion.choices[0].message)