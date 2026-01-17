# Project Requirements: Czech Weather Web Application

## Overview
A simple Flask web application that displays weather information for cities in the Czech Republic using the Open-Meteo API.

---

## Functional Requirements

### Core Features
| ID | Feature | Description | Priority |
|----|---------|-------------|----------|
| F1 | City Selection | Dropdown to select from predefined Czech cities | Must Have |
| F2 | Weather Display | Show current weather data (temp, humidity, conditions) | Must Have |
| F3 | Form Validation | Server-side validation of form inputs | Must Have |
| F4 | Error Handling | Graceful handling of API failures and invalid inputs | Must Have |

### User Interface
| ID | Feature | Description | Priority |
|----|---------|-------------|----------|
| U1 | Responsive Design | Mobile-friendly layout using Pico CSS v2 | Must Have |
| U2 | City Dropdown | Select element populated from `/api/cities` endpoint | Must Have |
| U3 | Weather Cards | Visual display of weather information | Must Have |

---

## Technical Requirements

### Stack & Dependencies
| Component | Technology | Notes |
|-----------|------------|-------|
| Language | Python 3.11+ | |
| Framework | Flask | Lightweight web framework |
| CSS Framework | Pico CSS v2 | Minimal, classless CSS |
| Dependency Manager | uv | Fast Python package manager |
| Weather API | Open-Meteo | Free, no API key required |

### Architecture Requirements
| ID | Requirement | Description |
|----|-------------|-------------|
| T1 | External CSS | All styles in separate `.css` file(s) |
| T2 | Jinja2 Macros | Reusable template components (forms, cards) |
| T3 | Form Validation | Validate selected city against allowed list |
| T4 | Cities Endpoint | `GET /api/cities` returns list of available cities |
| T5 | Environment Variables | Config via `.env` file |

---

## Project Structure
```
czech-weather-app/
├── app/
│   ├── __init__.py               # Flask app factory
│   ├── routes.py                 # Route handlers
│   ├── forms.py                  # Form definitions
│   ├── services/
│   │   └── weather_api.py        # Open-Meteo API client
│   ├── static/
│   │   └── css/
│   │       └── style.css         # Custom styles (extends Pico)
│   └── templates/
│       ├── base.html             # Base template with Pico CSS
│       ├── macros/
│       │   ├── forms.html        # Form component macros
│       │   └── weather.html      # Weather display macros
│       └── index.html            # Main page
├── .env.example                  # Template for environment variables
├── .gitignore                    # Exclude .env, __pycache__, etc.
├── pyproject.toml                # uv/Python project config
├── uv.lock                       # Locked dependencies
└── README.md
```

---

## API Endpoints

### Application Routes
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Main page with city selector and weather display |
| GET | `/api/cities` | Returns JSON list of available Czech cities |
| POST | `/weather` | Fetches weather for selected city |

### Cities Endpoint Response
```json
{
  "cities": [
    {"name": "Praha", "latitude": 50.0755, "longitude": 14.4378},
    {"name": "Brno", "latitude": 49.1951, "longitude": 16.6068},
    {"name": "Ostrava", "latitude": 49.8209, "longitude": 18.2625}
  ]
}
```

---

## Secrets Management

### .gitignore Must Include
- `.env`
- `__pycache__/`
- `*.pyc`
- `.venv/`

### Environment Variables Template (.env.example)
```bash
# Flask Configuration
FLASK_APP=app
FLASK_ENV=development
SECRET_KEY=change-this-secret-key

# Open-Meteo (no API key needed, but base URL configurable)
WEATHER_API_URL=https://api.open-meteo.com/v1
```

---

## Open-Meteo API

### Overview
- **Free** and **open-source**
- **No API key required**
- Supports Czech cities via coordinates

### Example Request
```
GET https://api.open-meteo.com/v1/forecast?latitude=50.0755&longitude=14.4378&current_weather=true
```

### Example Response
```json
{
  "current_weather": {
    "temperature": 12.5,
    "windspeed": 8.2,
    "winddirection": 180,
    "weathercode": 3,
    "time": "2026-01-17T14:00"
  }
}
```

### Weather Codes Reference
| Code | Description |
|------|-------------|
| 0 | Clear sky |
| 1-3 | Partly cloudy |
| 45, 48 | Fog |
| 51-55 | Drizzle |
| 61-65 | Rain |
| 71-75 | Snow |
| 95 | Thunderstorm |