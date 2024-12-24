from base import Base
import enum

from sqlalchemy import Column, String, Integer, Enum, Float

class OsType(enum.Enum):
  ios = "iOS"
  android = "Android"

class Phone(Base):
    __tablename__ = "phones"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    screenDiagonal = Column(Float, nullable=False)
    builtInMemory = Column(Integer, nullable=False)
    osType = Column(Enum(OsType), default=OsType.android, nullable=False)
    image = Column(String, nullable=False)
    price = Column(Integer, nullable=False)