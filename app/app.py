
import os
import openai
openai.api_key = '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'

completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
    {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
  ]
)

print(completion.choices[0].message)