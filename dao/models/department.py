from sqlalchemy import Column, Integer, String

from dao.models.base_model import Base


# ----------------------------------------------------------------------------------------------------------------------
class Department(Base):
    __tablename__ = 'departments'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), unique=True)
