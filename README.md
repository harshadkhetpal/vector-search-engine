# 🔍 Vector Search Engine — Qdrant + Weaviate + Pinecone Benchmark

[![FastAPI](https://img.shields.io/badge/FastAPI-0.111-009688?style=flat-square&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com)
[![Qdrant](https://img.shields.io/badge/Qdrant-1.9-DC143C?style=flat-square)](https://qdrant.tech)
[![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=flat-square&logo=python&logoColor=white)](https://python.org)
[![Docker](https://img.shields.io/badge/Docker-Ready-2496ED?style=flat-square&logo=docker&logoColor=white)](https://docker.com)

> Multi-backend semantic search engine with pluggable vector stores (Qdrant, Weaviate, Pinecone, pgvector). Includes benchmarks across 1M vectors and production-ready FastAPI service.

## 🏗 Architecture
```
Query → Embedding (BGE-M3/E5-large) → Vector DB (Qdrant/Weaviate) → Ranked Results
```

## 📊 Benchmark (1M vectors, dim=768)
| Backend | Latency p50 | Latency p99 | QPS | Recall@10 |
|---|---|---|---|---|
| Qdrant (HNSW) | 3ms | 12ms | 4,200 | 0.98 |
| Weaviate | 5ms | 18ms | 2,800 | 0.97 |
| Pinecone (pod) | 8ms | 25ms | 1,900 | 0.96 |
| pgvector | 45ms | 120ms | 450 | 0.94 |

## 🚀 Quick Start
```bash
git clone https://github.com/harshadkhetpal/vector-search-engine
cd vector-search-engine
docker-compose up -d
# Ingest sample data
python scripts/ingest.py --backend qdrant --collection products --dim 768
# Query
curl -X POST http://localhost:8000/search \
  -H "Content-Type: application/json" \
  -d '{"query": "wireless noise cancelling headphones", "top_k": 10}'
```
