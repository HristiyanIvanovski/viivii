import weaviate

client = weaviate.connect_to_local(port=8085)

questions = client.collections.get("Question")

response = questions.generate.near_text(
    query="two related facts on a random topic",
    limit=1,
    grouped_task="Write a tweet about these facts and how they relate to each other. Do it in Elon Musk's style and voice, say something controversial. Don't use hashtags.",
)

print(response.generated)

client.close()