# Czech Weather

Flask web application that displays current weather for cities in the Czech Republic using the Open-Meteo API.

## Quick Start

### 1. Install uv

**macOS/Linux:**

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**Windows (PowerShell):**

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

**Homebrew (macOS):**

```bash
brew install uv
```

After installation, restart your terminal or source your shell config.

### 2. Install Dependencies

```bash
uv sync
```

### 3. Configure Environment

```bash
cp .env.example .env
```

### 4. Run the Application

```bash
uv run flask run
```

Application available at **http://localhost:5000**

## Commands

### Application

```bash
uv run flask run     # Start development server
```

### Code Quality

```bash
uv run ruff check .        # Lint
uv run ruff check . --fix  # Lint and auto-fix
uv run ruff format .       # Format
uv run mypy app            # Type check
uv run pytest              # Run tests
```

## Project Structure

```
czech-weather/
├── app/
│   ├── __init__.py           # Flask app factory
│   ├── config.py             # Pydantic Settings configuration
│   ├── models.py             # Pydantic models (City, WeatherData)
│   ├── forms.py              # WTForms definitions
│   ├── errors.py             # Error handlers (404, 500)
│   ├── middleware/
│   │   ├── __init__.py
│   │   ├── logging.py        # Request logging + request ID
│   │   ├── security.py       # Security headers (CSP, XSS, etc.)
│   │   └── services.py       # Dependency injection
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── health.py         # Health check endpoints (/health, /ready)
│   │   └── weather.py        # Weather routes
│   ├── services/
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
├── .env.example
├── .gitignore
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

## Dependencies

| Package          | Purpose                    |
|------------------|----------------------------|
| flask            | Web framework              |
| flask-wtf        | Form handling              |
| httpx            | HTTP client                |
| pydantic-settings| Configuration management   |
| python-dotenv    | Environment file loading   |

### Dev Dependencies

| Package       | Purpose          |
|---------------|------------------|
| ruff          | Linter/formatter |
| mypy          | Type checking    |
| pytest        | Testing          |
| types-wtforms | Type stubs       |

## Tech Stack

- **Backend:** Python 3.11+ / Flask
- **Frontend:** [Pico CSS v2](https://picocss.com/)
- **API:** [Open-Meteo](https://open-meteo.com/) (free, no API key)
- **Package Manager:** [uv](https://docs.astral.sh/uv/)
