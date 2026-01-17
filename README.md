# Czech Weather App

A simple Flask web application that displays weather information for cities in the Czech Republic using the Open-Meteo API.

## Features

- 🏙️ Select from 10 Czech cities
- 🌡️ Current temperature display
- 💨 Wind speed and direction
- 🎨 Clean, responsive UI with Pico CSS v2
- ✅ Server-side form validation

## Tech Stack

- **Backend**: Python 3.11+ / Flask
- **Frontend**: Pico CSS v2
- **API**: Open-Meteo (free, no API key required)
- **Package Manager**: uv

## Quick Start

### 1. Install dependencies

```bash
uv sync
```

### 2. Set up environment

```bash
cp .env.example .env
```

### 3. Run the application

```bash
uv run flask run
```

The app will be available at `http://localhost:5000`

## Project Structure

```
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
├── .env.example              # Environment template
├── .gitignore
├── pyproject.toml
└── README.md
```

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Main page with city selector |
| GET | `/api/cities` | JSON list of available cities |
| POST | `/weather` | Fetch weather for selected city |

## Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `FLASK_APP` | Flask application module | `app` |
| `FLASK_ENV` | Environment (development/production) | `development` |
| `SECRET_KEY` | Flask secret key | - |
| `WEATHER_API_URL` | Open-Meteo API base URL | `https://api.open-meteo.com/v1` |

## License

MIT
