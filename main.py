import torch
from dotenv import load_dotenv
import os
from openai import OpenAI


# print pytorch version
print(torch.__version__)
print("A.I. Foundations Bootcamp Course Folder")


# Load the .env file
load_dotenv()


# get openAI api key from .env
client = OpenAI(
  api_key=os.environ.get("API_KEY"),
)




# need to add tokens but works
# completion = client.chat.completions.create(
#   model="gpt-3.5-turbo",
#   messages=[
#     {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
#     {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
#   ]
# )

# print(completion.choices[0].message)
