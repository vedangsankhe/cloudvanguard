from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.models.resource import Resource
from app.schemas.resource import ResourceOut

router = APIRouter(prefix="/api/v1/resources", tags=["resources"])


@router.get("", response_model=list[ResourceOut])
def list_resources(db: Session = Depends(get_db)):
    return db.scalars(select(Resource).order_by(Resource.id)).all()