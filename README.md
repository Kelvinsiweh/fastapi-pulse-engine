# FastAPI Pulse Engine

[![FastAPI](https://img.shields.io/badge/FastAPI-0.111+-009688.svg?style=flat&logo=FastAPI&logoColor=white)](https://fastapi.tiangolo.com)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A clean, modern, asynchronous enterprise REST API microservice showcasing structured dependency injection, JWT authentication, SQLAlchemy ORM async transactions, and automatic Swagger/OpenAPI documentation.

## Architecture Highlights
- **FastAPI**: Asynchronous route handlers and automatic OpenAPI 3.1 docs
- **Pydantic v2**: High-performance request/response data validation
- **SQLAlchemy 2.0**: Typed async ORM database repositories
- **Security**: OAuth2 Password bearer flow with signed JWT tokens

## Running the API Locally
```bash
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
```
Access API docs at `http://localhost:8000/docs`.

### cURL Example
```bash
curl -X GET http://localhost:8000/health
```
