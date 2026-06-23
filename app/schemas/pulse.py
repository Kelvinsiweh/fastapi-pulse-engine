from datetime import datetime
from typing import Optional
from pydantic import BaseModel, EmailStr, Field

class UserBase(BaseModel):
    email: EmailStr
    full_name: Optional[str] = None
    is_active: Optional[bool] = True

class UserCreate(UserBase):
    password: str = Field(..., min_length=8)

class UserResponse(UserBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True

class Token(BaseModel):
    access_token: str
    token_type: str

class MetricCreate(BaseModel):
    service_name: str
    cpu_usage: float = Field(..., ge=0.0, le=100.0)
    memory_mb: float = Field(..., ge=0.0)
    latency_ms: float = Field(..., ge=0.0)
    status: str = "healthy"

class MetricResponse(MetricCreate):
    id: int
    recorded_at: datetime

    class Config:
        from_attributes = True


# Enriched schema docs
