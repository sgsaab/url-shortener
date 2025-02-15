from sqlalchemy import Column, Integer, String
from .database import Base

class URL(Base):
    """SQLAlchemy model for URLs."""
    __tablename__ = "urls"

    id = Column(Integer, primary_key=True, index=True)
    original_url = Column(String, nullable=False)
    short_url = Column(String, unique=True, index=True, nullable=False)
    clicks = Column(Integer, default=0) 