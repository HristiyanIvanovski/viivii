import os

import weaviate
from weaviate.classes.init import Auth

client = weaviate.connect_to_local(
    port=8085, auth_credentials=Auth.api_key(os.environ["WEAVIATE_API_KEY"])
)

print(client.is_ready()) 

client.close()