from app.schemas import VoyageSimulationRequest, VoyageSimulationResult

def calculate_voyage_simulation(
    request: VoyageSimulationRequest,
) -> VoyageSimulationResult:
    vessel = request.vessel
    voyage = request.voyage

    estimated_hours = voyage.distance_nm / voyage.planned_speed_knots
    fuel_required = estimated_hours * vessel.fuel_burn_gph
    fuel_remaining = vessel.fuel_capacity_gallons - fuel_required

    fuel_reserve_percent = (fuel_remaining / vessel.fuel_capacity_gallons) * 100
    meets_reserve_requirement = fuel_reserve_percent >= vessel.reserve_requirement_percent

    warnings = []

    if fuel_remaining < 0:
        warnings.append("Fuel required exceeds vessel fuel capacity.")

    if not meets_reserve_requirement:
        warnings.append("Fuel reserve is below the vessel reserve requirement.")

    if voyage.planned_speed_knots > vessel.cruise_speed_knots:
        warnings.append("Planned speed exceeds the vessel's normal cruise speed.")

    risk_level = determine_risk_level(
        fuel_remaining=fuel_remaining,
        meets_reserve_requirement=meets_reserve_requirement,
        warning_count=len(warnings),
    )

    return VoyageSimulationResult(
        estimated_hours=round(estimated_hours, 2),
        fuel_required_gallons=round(fuel_required, 2),
        fuel_remaining_gallons=round(fuel_remaining, 2),
        fuel_reserve_percent=round(fuel_reserve_percent, 2),
        meets_reserve_requirement=meets_reserve_requirement,
        risk_level=risk_level,
        warnings=warnings,
    )

