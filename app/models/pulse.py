from datetime import datetime
from sqlalchemy import Column, Integer, String, Boolean, DateTime, Float, ForeignKey
from sqlalchemy.orm import relationship
from app.db.session import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    full_name = Column(String, nullable=True)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)

class ServiceMetric(Base):
    __tablename__ = "service_metrics"

    id = Column(Integer, primary_key=True, index=True)
    service_name = Column(String, index=True, nullable=False)
    cpu_usage = Column(Float, nullable=False)
    memory_mb = Column(Float, nullable=False)
    latency_ms = Column(Float, nullable=False)
    status = Column(String, default="healthy")
    recorded_at = Column(DateTime, default=datetime.utcnow)
