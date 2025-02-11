import weaviate

client = weaviate.connect_to_local(port=8085)

questions = client.collections.get("Question")

response = questions.generate.near_text(
    query="science",
    limit=1,
    grouped_task="Write a tweet about this fact. Do it in Elon Musk's style and voice, say something controversial. Don't use hashtags."
)

print(response.generated)

client.close()