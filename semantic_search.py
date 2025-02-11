import weaviate
import json

client = weaviate.connect_to_local(port=8085)

questions = client.collections.get("Question")

response = questions.query.near_text(
    query="biology",
    limit=None
)

for obj in response.objects:
    print(json.dumps(obj.properties, indent=2))

client.close()