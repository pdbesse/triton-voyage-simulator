# Triton API

A FastAPI-based voyage simulation API that calculates fuel usage, voyage
feasibility, reserve compliance, and estimated travel times for
recreational and commercial vessels.

## Features

-   RESTful API built with FastAPI
-   Interactive Swagger UI (`/docs`)
-   Voyage simulation endpoint
-   Fuel burn and reserve calculations
-   Configurable vessel characteristics
-   Automatic validation with Pydantic
-   Docker-ready project structure

## Project Structure

``` text
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

## Installation

``` bash
git clone https://github.com/<your-username>/triton.git
cd triton

python -m venv venv

# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate

pip install -r requirements.txt
```

## Running the API

``` bash
uvicorn app.main:app --reload
```

Open:

-   http://127.0.0.1:8000/docs
-   http://127.0.0.1:8000/redoc

## Example Request

``` json
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

``` json
{
  "distance_nm": 22.5,
  "estimated_time_hours": 1.02,
  "fuel_required_gallons": 18.4,
  "fuel_remaining_gallons": 181.6,
  "reserve_met": true,
  "voyage_possible": true
}
```

## Roadmap

-   Weather integration
-   Tide/current modeling
-   Route optimization
-   Marina fuel pricing
-   AIS integration
-   Authentication

## License

MIT License
