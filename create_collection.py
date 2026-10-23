import os

import weaviate
from weaviate.classes.init import Auth
from weaviate.classes.config import Configure

client = weaviate.connect_to_local(
    port=8085, auth_credentials=Auth.api_key(os.environ["WEAVIATE_API_KEY"])
)

questions = client.collections.create(
    name="Question",
    vectorizer_config=Configure.Vectorizer.text2vec_ollama(
        api_endpoint="http://host.docker.internal:11434",  
        model="nomic-embed-text",                          
    ),
    generative_config=Configure.Generative.ollama(         
        api_endpoint="http://host.docker.internal:11434",  
        model="llama3.2",                                  
    )
)

client.close()