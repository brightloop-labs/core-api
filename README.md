# core-api

Order management backend service for Brightloop Labs' internal platform.

## Stack
- FastAPI
- PostgreSQL (SQLAlchemy + Alembic)
- Docker / docker-compose for local development

## Getting started

```bash
docker-compose up --build
```

The API will be available at `http://localhost:8000`.

## API examples

Create an order:

```bash
curl -X POST http://localhost:8000/orders/ \
  -H "Content-Type: application/json" \
  -d '{"customer_email": "jane@example.com", "total_amount": 49.99}'
```

List orders:

```bash
curl http://localhost:8000/orders/
```