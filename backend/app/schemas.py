from typing import List
from pydantic import BaseModel, Field

class Vessel(BaseModel):
    name: str = Field(..., example="Example Vessel")
    vessel_type: str = Field(..., example="powerboat")
    length_ft: float = Field(..., gt=0, example=32)
    fuel_capacity_gallons: float = Field(..., gt=0, example=200)
    cruise_speed_knotsL: float = Field(..., gt=0, example=22)
    fuel_burn_gph: float = Field(..., ge=0, example=18)
    reserve_requirement_percent: float = Field(..., ge=0, le=100, example=20)

class Voyage(BaseModel):
    start_name: str = Field(..., example="Plymouth, MA")
    end_name: str = Field(..., example='Provincetown, MA')
    distance_nm: float = Field(..., gt=0, example=22.5)
    planned_speed_knots: float = Field(..., gt=0, example=22)

