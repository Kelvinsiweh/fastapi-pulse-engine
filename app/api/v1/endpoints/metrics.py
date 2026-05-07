from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.db.session import get_db
from app.models.pulse import ServiceMetric, User
from app.schemas.pulse import MetricCreate, MetricResponse
from app.api.deps import get_current_user

router = APIRouter()

@router.post("/", response_model=MetricResponse)
async def record_metric(
    metric_in: MetricCreate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    metric = ServiceMetric(**metric_in.model_dump())
    db.add(metric)
    await db.commit()
    await db.refresh(metric)
    return metric

@router.get("/", response_model=List[MetricResponse])
async def list_metrics(
    skip: int = 0,
    limit: int = 50,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    query = await db.execute(select(ServiceMetric).offset(skip).limit(limit))
    return query.scalars().all()
