from fastapi_users.db import SQLAlchemyBaseUserTableUUID
from sqlalchemy import Column, String
from src.db import Base
from typing import Optional


class User(SQLAlchemyBaseUserTableUUID, Base):
    first_name = Column(String(50), nullable=True)
    last_name = Column(String(50), nullable=True)