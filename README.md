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

```bash
uv sync              # Install dependencies
uv run flask run     # Start development server
uv add <package>     # Add new dependency
uv remove <package>  # Remove dependency
```

## Project Structure

```
czech-weather/
├── app/
│   ├── __init__.py           # Flask app factory
│   ├── routes.py             # Route handlers
│   ├── forms.py              # WTForms definitions
│   ├── services/
│   │   └── weather_api.py    # Open-Meteo API client
│   ├── static/
│   │   └── css/
│   │       └── style.css     # Custom styles
│   └── templates/
│       ├── base.html         # Base template
│       ├── index.html        # Main page
│       └── macros/
│           ├── forms.html    # Form components
│           └── weather.html  # Weather display components
├── .env.example
├── .gitignore
├── pyproject.toml
└── README.md
```

## API Endpoints

| Method | Endpoint      | Description                    |
|--------|---------------|--------------------------------|
| GET    | `/`           | Main page with city selector   |
| GET    | `/api/cities` | JSON list of available cities  |
| POST   | `/weather`    | Fetch weather for selected city |

## Environment Variables

| Variable          | Default                          | Description            |
|-------------------|----------------------------------|------------------------|
| `FLASK_APP`       | `app`                            | Flask application      |
| `FLASK_ENV`       | `development`                    | Environment mode       |
| `SECRET_KEY`      | -                                | Flask secret key       |
| `WEATHER_API_URL` | `https://api.open-meteo.com/v1`  | Open-Meteo API base URL |

## Dependencies

| Package       | Purpose              |
|---------------|----------------------|
| flask         | Web framework        |
| flask-wtf     | Form handling        |
| python-dotenv | Environment config   |
| requests      | HTTP client          |

## Tech Stack

- **Backend:** Python 3.11+ / Flask
- **Frontend:** [Pico CSS v2](https://picocss.com/)
- **API:** [Open-Meteo](https://open-meteo.com/) (free, no API key)
- **Package Manager:** [uv](https://docs.astral.sh/uv/)
