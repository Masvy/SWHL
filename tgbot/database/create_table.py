from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, VARCHAR, DATE, Integer

BaseModel = declarative_base()


class NewUser(BaseModel):
    __tablename__ = 'new_users'

    id_ = Column(Integer, unique=True, autoincrement=True, primary_key=True)

    full_name = Column(VARCHAR(50), unique=False, nullable=True)

    birthday = Column(DATE, nullable=True)

    stick_grip = Column(VARCHAR(6), unique=False, nullable=True)

    phoro = Column(VARCHAR(100), unique=False, nullable=True)
