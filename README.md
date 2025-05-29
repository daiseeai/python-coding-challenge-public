# Python: `FastAPI`/SQL Database Management Challenge.

[![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)](https://fastapi.tiangolo.com/)
[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org)
[![SQLite](https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white)](https://www.sqlite.org)
[![JWT](https://img.shields.io/badge/JWT-black?style=for-the-badge&logo=JSON%20web%20tokens)](https://jwt.io)

# Overview
* A `FastAPI` based challenge. 
* Focussed around the age-old `Ecommerce` [CRUD](https://www.codecademy.com/article/what-is-crud) use case.
* Your challenge is to investigate the current `app` which uses `SQLite` to generate an example database and define some stub `schemas and models` for use with the `FastAPI` app.

## What's Already Here?

- `RESTful` API for product management.
    - The skeleton code for this is already provided.
- `SQLite` database with sample data generation.
    - Using `Faker` to generate fake DB entries.
- `JWT` authentication.
    - For this case any random string will be a `"valid token"`.
- Input validation using `Pydantic`.

## What's Your Task?
- See [this challenge file](./challenge.md) for more information.

# Setup

1. Create and activate virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
uvicorn app.main:app --reload
```

> [!Note]
> This creates a `test.db` file with sample data.
> If you are wanting to refresh this/re-generate you can simply remove the `test.db` file.
> IF this does not exist on running of the app it will be created.

4. (Optional): At this point you can interact with the database through CLI.

    4.1. `sqlite3 test.db`

    4.2. Then you can run test commands

> requires `sqlite` or and equivalent tool such as [`litecli`](https://litecli.com/)

> [!Example]
> ```sql
>    .tables           -- list tables
>   SELECT * FROM products;  -- show all products
>    .exit             -- exit shell
>   ```

## API Documentation

### Authentication
All endpoints require a Bearer token in the Authorization header:
```bash
Authorization: Bearer test-token
```

> [!Tip]
> For now this is a fake token.

### Core Endpoints

#### Health Check
```bash
curl -X GET "http://localhost:8000/health" \
  -H "Authorization: Bearer test-token"

{"status":"ok"}
```

> [!Note]
> As you complete the challenge more endpoints will be added here.
> Feel free to update the `README` if you wish.


# Appendix
## Database Schema

### Products Table
```sql
CREATE TABLE products (
    id VARCHAR NOT NULL PRIMARY KEY,
    name VARCHAR,
    description VARCHAR,
    price FLOAT,
    category VARCHAR,
    stock INTEGER,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME
);

-- Indexes
CREATE INDEX ix_products_category ON products (category);
CREATE INDEX ix_products_name ON products (name);
```

## Development

### Project Structure
```
python-fastapi/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── db.py
│   ├── models.py
│   ├── schemas.py
│   ├── auth.py
│   └── routers/
│       ├── __init__.py
│       └── products.py
├── tests/
    ├── TODO: Highly optional. 
├── requirements.txt
└── README.md
```

### Key Components
- `models.py`: SQLAlchemy models
- `schemas.py`: Pydantic models for request/response validation
- `db.py`: Database configuration and session management
- `routers/products.py`: Product-related endpoints
    - Creation of this is your is primarily your challenge.
- `auth.py`: Authentication middleware

### Testing
```bash
# Run tests
pytest
```

> [!Note]
> Unit testing optional if time is permitted.
