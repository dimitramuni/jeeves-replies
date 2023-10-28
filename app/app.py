import os
from langchain.llms import OpenAI

llm=OpenAI(temperature=0.8)
baby_name=llm('Suggest me 10 baby name for Indian girl from the Ramayana')
print(baby_name)