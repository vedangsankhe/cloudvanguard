from pydantic import BaseModel, ConfigDict


class ResourceOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    resource_id: str
    name: str
    resource_type: str
    region: str
    monthly_cost_usd: float
    cpu_utilization: float
    idle_days: int
    status: str