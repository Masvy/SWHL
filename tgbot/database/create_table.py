from sqlalchemy import Column, VARCHAR, BigInteger, Integer
from sqlalchemy.ext.declarative import declarative_base

BaseModel = declarative_base()


class NewPlayer(BaseModel):
    __tablename__ = 'new_players'

    id_ = Column(Integer, autoincrement=True, primary_key=True)

    user_id = Column(BigInteger, unique=False, nullable=True)

    full_name = Column(VARCHAR(50), unique=False, nullable=True)

    birthday = Column(VARCHAR(11), unique=False, nullable=True)

    stick_grip = Column(VARCHAR(6), unique=False, nullable=True)

    photo = Column(VARCHAR(100), unique=False, nullable=True)


class NewCommand(BaseModel):
    __tablename__ = 'new_commands'

    id_ = Column(Integer, autoincrement=True, primary_key=True)

    user_id = Column(BigInteger, unique=False, nullable=True)

    name = Column(VARCHAR(20), unique=False, nullable=True)

    foundation = Column(VARCHAR(11), unique=False, nullable=True)

    arena = Column(VARCHAR(20), unique=False, nullable=True)

    contact = Column(VARCHAR(50), unique=False, nullable=True)

    phone_number = Column(VARCHAR(11), unique=False, nullable=True)
