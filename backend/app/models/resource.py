from sqlalchemy import Float, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from app.core.database import Base


class Resource(Base):
    __tablename__ = "resources"

    id: Mapped[int] = mapped_column(primary_key=True)
    resource_id: Mapped[str] = mapped_column(String(50), unique=True)
    name: Mapped[str] = mapped_column(String(100))
    resource_type: Mapped[str] = mapped_column(String(30))
    region: Mapped[str] = mapped_column(String(30))
    monthly_cost_usd: Mapped[float] = mapped_column(Float)
    cpu_utilization: Mapped[float] = mapped_column(Float)
    idle_days: Mapped[int] = mapped_column(Integer)
    status: Mapped[str] = mapped_column(String(30), default="ACTIVE")