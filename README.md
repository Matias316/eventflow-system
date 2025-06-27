# 🚀 EventFlow System

A backend API service for scheduling, managing, and notifying events. Designed to demonstrate architectural best practices including background task orchestration, external API integration, and observability.

---

## 🛠️ Tech Stack

- **Backend Framework**: Flask
- **Database**: PostgreSQL
- **Async Tasks**: Celery + RabbitMQ
- **Cache**: Redis
- **Containerization**: Docker, docker-compose
- **CI/CD**: GitHub Actions
- **Monitoring **: TBD (Datadog?)
- **Infra **: Kubernetes YAMLs

---

## 📚 Features

- CRUD API for managing events
- Validation to prevent overlapping events at the same location
- Soft-delete logic (`is_deleted`)
- Background tasks to:
  - Send simulated notifications
  - Cache most popular events
- Exposes public events from a 3rd-party API
- CI pipeline for linting, testing, and Docker build
- Ready for observability and production-level structure

---

## 🚀 Getting Started

### Requirements

- Docker + docker-compose
- Python 3.9+ (if running locally)
- Poetry
- PostgreSQL, Redis, RabbitMQ

### How to Install and run locally (Poetry)

```bash
poetry install
poetry run flask run
```

### How to Build and Run (Docker)

```bash
docker-compose up --build
```

### How to run Tests (Poetry)

```bash
poetry run pytest
poetry run pytest --cov=app --cov-report=term --cov-report=html
```