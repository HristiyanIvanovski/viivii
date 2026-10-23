import os

import weaviate
from weaviate.classes.init import Auth
import json

client = weaviate.connect_to_local(
    port=8085, auth_credentials=Auth.api_key(os.environ["WEAVIATE_API_KEY"])
)

questions = client.collections.get("Question")

response = questions.query.near_text(
    query="biology",
    limit=None
)

for obj in response.objects:
    print(json.dumps(obj.properties, indent=2))

client.close()