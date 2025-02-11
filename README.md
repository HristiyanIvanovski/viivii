# Weaviate x Ollama | VectorDB + Semantic Search + RAG

This project demonstrates how to run and use Weaviate for importing and vectorizing data, to enable semantic search and retrieval-augmented generation (RAG). Integrating a dockerized Weaviate instance with a locally installed Ollama for text vectorization and generative modeling.

## Stack

- **Dockerized Weaviate:** Run as [docker-compose.yml](docker-compose.yml)
- **Local Ollama:** Provides the vectorizer and generative model

## Files & Their Roles | Run Sequence

1. [is_ready.py](is_ready.py): Checks if the Weaviate service is running.
2. [create_collection.py](create_collection.py): Creates the "Question" collection with vectorization and generative configurations.
3. [add_obj.py](add_obj.py): Imports question objects from JSON.
4. [semantic_search.py](semantic_search.py): Performs a semantic search query against the "Question" collection.
5. [quick_rag.py](quick_rag.py): Generates a tweet-styled response on a given topic.