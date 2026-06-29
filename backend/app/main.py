from fastapi import FastAPI

from app.schemas import VoyageSimulationRequest, VoyageSimulationResult
from app.simulation import calculate_voyage_simulation

app = FastAPI(
    title="Triton API",
    description="Maritime voyage planning and simulation API.",
    version="0.1.0",
)


@app.get("/")
def read_root():
    return {"message": "Triton API is running"}


@app.post("/simulations/voyage", response_model=VoyageSimulationResult)
def simulate_voyage(request: VoyageSimulationRequest):
    return calculate_voyage_simulation(request)