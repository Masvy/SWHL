from sqlalchemy import insert, update
from sqlalchemy.orm import sessionmaker
from database.create_table import NewPlayer


async def add_user_id(session_maker: sessionmaker, user_id):
    async with session_maker() as session:
        async with session.begin():
            await session.execute(insert(NewPlayer).values(user_id=user_id))


async def add_name(session_maker: sessionmaker, user_id, full_name):
    async with session_maker() as session:
        async with session.begin():
            await session.execute(update(NewPlayer).where(NewPlayer.user_id == user_id).values(full_name=full_name))


async def add_birthday(session_maker: sessionmaker, user_id, birthday):
    async with session_maker() as session:
        async with session.begin():
            await session.execute(update(NewPlayer).where(NewPlayer.user_id == user_id).values(birthday=birthday))


async def add_stick_grip(session_maker: sessionmaker, user_id, stick_grip):
    async with session_maker() as session:
        async with session.begin():
            await session.execute(update(NewPlayer).where(NewPlayer.user_id == user_id).values(stick_grip=stick_grip))


async def add_photo(session_maker: sessionmaker, user_id, photo):
    async with session_maker() as session:
        async with session.begin():
            await session.execute(update(NewPlayer).where(NewPlayer.user_id == user_id).values(photo=photo))
