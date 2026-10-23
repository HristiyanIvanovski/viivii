import os

import weaviate
from weaviate.classes.init import Auth

client = weaviate.connect_to_local(
    port=8085, auth_credentials=Auth.api_key(os.environ["WEAVIATE_API_KEY"])
)

questions = client.collections.get("Question")

#user input in terminal for query
query = input("Enter your query: ")

response = questions.generate.near_text(
    query=query,
    limit=1,
    grouped_task="Write a tweet about this fact. Do it in Elon Musk's style and voice, say something controversial. Don't use hashtags."
)

print(response.generated)

client.close()