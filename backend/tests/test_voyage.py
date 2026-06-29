from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def valid_payload():
    return {
        "vessel": {
            "name": "Example Vessel",
            "vessel_type": "powerboat",
            "length_ft": 32,
            "fuel_capacity_gallons": 200,
            "cruise_speed_knots": 22,
            "fuel_burn_gph": 18,
            "reserve_requirement_percent": 20,
        },
        "voyage": {
            "start_name": "Plymouth, MA",
            "end_name": "Provincetown, MA",
            "distance_nm": 22.5,
            "planned_speed_knots": 22,
        },
    }


def test_voyage_simulation_success():
    response = client.post("/simulations/voyage", json=valid_payload())

    assert response.status_code == 200

    data = response.json()

    assert data["estimated_hours"] == 1.02
    assert data["fuel_required_gallons"] == 18.41
    assert data["fuel_remaining_gallons"] == 181.59
    assert data["fuel_reserve_percent"] == 90.8
    assert data["meets_reserve_requirement"] is True
    assert data["risk_level"] == "LOW"
    assert data["warnings"] == []


def test_voyage_with_insufficient_fuel_is_critical_risk():
    payload = valid_payload()
    payload["vessel"]["fuel_capacity_gallons"] = 10

    response = client.post("/simulations/voyage", json=payload)

    assert response.status_code == 200

    data = response.json()

    assert data["fuel_remaining_gallons"] < 0
    assert data["meets_reserve_requirement"] is False
    assert data["risk_level"] == "CRITICAL"
    assert "Fuel required exceeds vessel fuel capacity." in data["warnings"]
    assert "Fuel reserve is below the vessel reserve requirement." in data["warnings"]


def test_voyage_reserve_not_met_is_high_risk():
    payload = valid_payload()
    payload["vessel"]["fuel_capacity_gallons"] = 25
    payload["vessel"]["reserve_requirement_percent"] = 50

    response = client.post("/simulations/voyage", json=payload)

    assert response.status_code == 200

    data = response.json()

    assert data["fuel_remaining_gallons"] == 6.59
    assert data["meets_reserve_requirement"] is False
    assert data["risk_level"] == "HIGH"
    assert "Fuel reserve is below the vessel reserve requirement." in data["warnings"]


def test_invalid_negative_distance_returns_validation_error():
    payload = valid_payload()
    payload["voyage"]["distance_nm"] = -5

    response = client.post("/simulations/voyage", json=payload)

    assert response.status_code == 422


def test_invalid_zero_speed_returns_validation_error():
    payload = valid_payload()
    payload["voyage"]["planned_speed_knots"] = 0

    response = client.post("/simulations/voyage", json=payload)

    assert response.status_code == 422


def test_missing_vessel_returns_validation_error():
    payload = valid_payload()
    del payload["vessel"]

    response = client.post("/simulations/voyage", json=payload)

    assert response.status_code == 422


def test_missing_voyage_returns_validation_error():
    payload = valid_payload()
    del payload["voyage"]

    response = client.post("/simulations/voyage", json=payload)

    assert response.status_code == 422