from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

Base = declarative_base()
engine = create_engine("postgresql://study_user:your_password@postgres:5432/study_db")

class Problem(Base):
    __tablename__ = "problems"
    id = Column(Integer, primary_key=True)
    topic = Column(String(255))
    question = Column(Text)
    answer = Column(Text)
    created_at = Column(DateTime, server_default="CURRENT_TIMESTAMP")
    updated_at = Column(DateTime, server_default="CURRENT_TIMESTAMP")
