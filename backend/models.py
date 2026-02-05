from sqlalchemy import Column, Float, JSON, String, DateTime
from database import Base

class CVE(Base):
    __tablename__ = "recipes"

    id = Column(String, primary_key=True, index=True)
    identifier = Column(String, index=True)
    description = Column(String)
    published_date = Column(DateTime)
    last_modified_date = Column(DateTime)
    base_score = Column(Float, nullable=True)