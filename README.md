# Triton
[![Python Tests](https://github.com/pdbesse/triton-voyage-simulator/actions/workflows/python-tests.yml/badge.svg)](https://github.com/pdbesse/triton-voyage-simulator/actions/workflows/python-tests.yml)
### Intelligent Voyage Planning API for Recreational & Commercial Vessels

> A FastAPI application that simulates marine voyages by calculating travel time, fuel consumption, reserve compliance, and voyage feasibility from vessel and route characteristics.

---

## Overview

Triton was built as a backend API that demonstrates clean software architecture, REST API design, data validation, and domain modeling using a real-world marine use case.

Given vessel specifications and voyage details, Triton determines:

- Estimated travel time
- Fuel consumption
- Fuel remaining after arrival
- Reserve fuel compliance
- Overall voyage feasibility

The project emphasizes readable code, strong validation, and extensibility for future marine navigation features.

---

## Features

- FastAPI REST API
- Automatic OpenAPI documentation
- Pydantic request/response validation
- Voyage simulation engine
- Fuel burn calculations
- Reserve fuel verification
- Structured JSON responses
- Modular project architecture

---

## Tech Stack

| Technology | Purpose |
|------------|---------|
| Python 3 | Core language |
| FastAPI | REST API framework |
| Pydantic | Validation & serialization |
| Uvicorn | ASGI server |
| Swagger UI | Interactive API documentation |

---

## Project Structure

```text
triton/
├── app/
│   ├── main.py
│   ├── models.py
│   ├── routes.py
│   ├── services.py
│   └── __init__.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Installation

```bash
git clone https://github.com/YOUR_USERNAME/triton.git
cd triton

python -m venv venv

# Windows
venv\Scripts\activate

pip install -r requirements.txt
```

---

## Running the API

```bash
uvicorn app.main:app --reload
```

Open:

- http://127.0.0.1:8000/docs
- http://127.0.0.1:8000/redoc

---

## Example Request

```json
{
  "vessel": {
    "name": "Example Vessel",
    "vessel_type": "powerboat",
    "length_ft": 32,
    "fuel_capacity_gallons": 200,
    "cruise_speed_knots": 22,
    "fuel_burn_gph": 18,
    "reserve_requirement_percent": 20
  },
  "voyage": {
    "start_name": "Plymouth, MA",
    "end_name": "Provincetown, MA",
    "distance_nm": 22.5,
    "planned_speed_knots": 22
  }
}
```

## Example Response

```json
{
  "distance_nm": 22.5,
  "estimated_time_hours": 1.02,
  "fuel_required_gallons": 18.4,
  "fuel_remaining_gallons": 181.6,
  "reserve_met": true,
  "voyage_possible": true
}
```

---

## API Endpoint

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/simulations/voyage` | Simulate a voyage and return fuel and travel calculations |

---

## Future Enhancements

- Weather integration
- NOAA tide & current data
- Route optimization
- AIS vessel integration
- Marina fuel pricing
- User authentication
- Historical voyage storage
- Docker deployment
- CI/CD with GitHub Actions

---

## Why This Project?

Triton demonstrates practical backend engineering skills by combining API development, data modeling, validation, and business logic into a clean, maintainable application. Rather than being a simple CRUD project, it models a real-world operational problem in the marine domain and is designed to serve as the foundation for more advanced voyage planning capabilities.

---

## License

This project is licensed under the MIT License.

---

## Author

**Phillip Besse**

M.S. Computer Science

Marine Operations • Backend Development • Python • FastAPI
