# Czech Weather

Flask web application that displays current weather for cities in the Czech Republic using the Open-Meteo API.

## Quick Start

```bash
docker compose up --build
```

Application available at **http://localhost:8000**

This will:
- Build the application image
- Start PostgreSQL database
- Run migrations and seed data
- Start the application with Gunicorn

### Stop

```bash
docker compose down      # Stop containers
docker compose down -v   # Stop and remove database volume
```

---

## Local Development

### Prerequisites

Install [uv](https://docs.astral.sh/uv/):

```bash
# macOS/Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Homebrew
brew install uv
```

### Setup

```bash
uv sync                           # Install dependencies
cp .env.example .env              # Configure environment
docker compose up -d database     # Start PostgreSQL only
uv run alembic upgrade head       # Run migrations
uv run python -m scripts.seed     # Seed database
uv run flask run                  # Start dev server
```

### Commands

```bash
# Application
uv run flask run                  # Start development server

# Database
uv run alembic upgrade head       # Run migrations
uv run alembic downgrade -1       # Rollback last migration
uv run alembic history            # Show migration history
uv run python -m scripts.seed     # Seed database

# Code Quality
uv run ruff check .               # Lint
uv run ruff check . --fix         # Lint and auto-fix
uv run ruff format .              # Format
uv run mypy app                   # Type check

# Testing
uv run playwright install chromium  # First time only
uv run pytest                       # Run all tests (headless)
uv run pytest --headed              # Run with visible browser
```

## Project Structure

```
czech-weather/
├── app/
│   ├── __init__.py           # Flask app factory
│   ├── config.py             # Pydantic Settings configuration
│   ├── database.py           # SQLModel engine and session
│   ├── forms.py              # WTForms definitions
│   ├── errors.py             # Error handlers (404, 500)
│   ├── models/
│   │   ├── __init__.py
│   │   ├── city.py           # City SQLModel
│   │   ├── weather_code.py   # WeatherCode SQLModel
│   │   └── weather_data.py   # WeatherData Pydantic model
│   ├── middleware/
│   │   ├── __init__.py
│   │   ├── logging.py        # Request logging + request ID
│   │   ├── security.py       # Security headers (CSP, XSS, etc.)
│   │   ├── services.py       # Dependency injection
│   │   └── validation.py     # Form validation decorator
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── health.py         # Health check endpoints (/health, /ready)
│   │   └── weather.py        # Weather routes
│   ├── services/
│   │   ├── __init__.py
│   │   └── weather.py        # Open-Meteo API client
│   ├── static/
│   │   └── css/
│   │       └── style.css
│   └── templates/
│       ├── base.html
│       ├── index.html
│       ├── errors/
│       │   ├── 404.html
│       │   └── 500.html
│       └── macros/
│           ├── forms.html
│           └── weather.html
├── migrations/
│   ├── env.py
│   ├── script.py.mako
│   └── versions/
│       └── 001_initial_schema.py
├── scripts/
│   └── seed.py               # Database seeding script
├── tests/
│   ├── conftest.py           # Pytest fixtures
│   └── test_e2e.py           # End-to-end tests
├── .dockerignore
├── .env.example
├── .gitignore
├── alembic.ini
├── compose.yml
├── Dockerfile
├── pyproject.toml
└── README.md
```

## API Endpoints

| Method | Endpoint      | Description                     |
|--------|---------------|---------------------------------|
| GET    | `/`           | Main page with city selector    |
| GET    | `/api/cities` | JSON list of available cities   |
| POST   | `/weather`    | Fetch weather for selected city |
| GET    | `/health`     | Liveness probe (Kubernetes)     |
| GET    | `/ready`      | Readiness probe (Kubernetes)    |

## Environment Variables

| Variable              | Default                         | Description             |
|-----------------------|---------------------------------|-------------------------|
| `SECRET_KEY`          | `dev-secret-key...`             | Flask secret key        |
| `DEBUG`               | `false`                         | Debug mode              |
| `WEATHER_API_URL`     | `https://api.open-meteo.com/v1` | Open-Meteo API base URL |
| `WEATHER_API_TIMEOUT` | `10`                            | API request timeout     |
| `PGHOST`              | `localhost`                     | PostgreSQL host         |
| `PGPORT`              | `5432`                          | PostgreSQL port         |
| `PGUSER`              | `postgres`                      | PostgreSQL user         |
| `PGPASSWORD`          | `postgres`                      | PostgreSQL password     |
| `PGDATABASE`          | `czech_weather`                 | PostgreSQL database     |

## Dependencies

| Package           | Purpose                     |
|-------------------|-----------------------------|
| flask             | Web framework               |
| flask-wtf         | Form handling               |
| gunicorn          | Production WSGI server      |
| httpx             | HTTP client                 |
| pydantic-settings | Configuration management    |
| python-dotenv     | Environment file loading    |
| sqlmodel          | ORM (SQLAlchemy + Pydantic) |
| psycopg           | PostgreSQL driver           |
| alembic           | Database migrations         |

### Dev Dependencies

| Package           | Purpose              |
|-------------------|----------------------|
| ruff              | Linter/formatter     |
| mypy              | Type checking        |
| pytest            | Testing              |
| pytest-playwright | E2E browser testing  |
| types-wtforms     | Type stubs           |

## Tech Stack

- **Backend:** Python 3.11+ / Flask
- **Database:** PostgreSQL 17
- **ORM:** SQLModel
- **Frontend:** [Pico CSS v2](https://picocss.com/)
- **API:** [Open-Meteo](https://open-meteo.com/) (free, no API key)
- **Testing:** Pytest + Playwright
- **Package Manager:** [uv](https://docs.astral.sh/uv/)
