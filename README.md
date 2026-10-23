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

## Authentication

Anonymous access is disabled. Weaviate requires an API key, read from the `WEAVIATE_API_KEY` environment variable by both `docker-compose.yml` and the Python scripts.

```bash
cp .env.example .env                                         # .env is git-ignored
sed -i '' "s/change-me/$(openssl rand -hex 32)/" .env        # macOS; on Linux use sed -i
docker compose up -d                                         # Compose reads .env automatically
set -a; source .env; set +a                                  # export the key for the Python scripts
python is_ready.py
```

The key belongs to the `viivii` user, which is the RBAC root user. Ports 8085 (HTTP) and 50051 (gRPC) are bound to `127.0.0.1` only.

Upgrading an existing `weaviate_data` volume from 1.28: Weaviate recommends upgrading one minor version at a time. For this demo, the simplest path is `docker compose down -v`, then re-run the scripts from step 2 to recreate and re-import the data.

