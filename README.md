#  Product Catalog Service

A robust backend microservice for managing products and categories in an e-commerce platform.

Built using:

- FastAPI
- PostgreSQL
- SQLAlchemy
- Repository Pattern
- Unit of Work Pattern
- Docker
- Pytest

---

##  Features

- Full CRUD for Products
- Full CRUD for Categories
- Advanced Search (keyword, category, price range)
- Repository Pattern implementation
- Unit of Work for transactional integrity
- Database seeding
- Dockerized setup
- Unit and Integration tests
- Swagger/OpenAPI documentation

---

##  Architecture

The project follows clean architecture principles:

### 1️ Repository Pattern
All database access is abstracted through repositories.
Service layer never directly interacts with the database.

### 2️ Unit of Work Pattern
Ensures atomic transactions across multiple repository operations.

### 3️ Service Layer
Contains business logic and orchestrates repositories.

---

##  Database Schema

### Products Table
- id (UUID, PK)
- name (TEXT)
- description (TEXT)
- price (DECIMAL)
- sku (UNIQUE)
- created_at
- updated_at

### Categories Table
- id (UUID, PK)
- name (UNIQUE)
- description

### product_categories
- product_id
- category_id

(Many-to-Many relationship)

---

##  Running with Docker

### Build and Start

```bash
docker-compose up --build