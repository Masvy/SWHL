from sqlalchemy import insert, update
from sqlalchemy.orm import sessionmaker
from database.create_table import NewCommand


async def add_user_id_com(session_maker: sessionmaker, user_id):
    async with session_maker() as session:
        async with session.begin():
            await session.execute(insert(NewCommand).values(user_id=user_id))


async def add_name_com(session_maker: sessionmaker, user_id, name):
    async with session_maker() as session:
        async with session.begin():
            await session.execute(update(NewCommand).where(NewCommand.user_id == user_id).values(name=name))


async def add_foundation(session_maker: sessionmaker, user_id, foundation):
    async with session_maker() as session:
        async with session.begin():
            await session.execute(update(NewCommand).where(NewCommand.user_id == user_id).values(foundation=foundation))


async def add_arena(session_maker: sessionmaker, user_id, arena):
    async with session_maker() as session:
        async with session.begin():
            await session.execute(update(NewCommand).where(NewCommand.user_id == user_id).values(arena=arena))


async def add_contact(session_maker: sessionmaker, user_id, contact):
    async with session_maker() as session:
        async with session.begin():
            await session.execute(update(NewCommand).where(NewCommand.user_id == user_id).values(contact=contact))


async def add_phone_number(session_maker: sessionmaker, user_id, phone_number):
    async with session_maker() as session:
        async with session.begin():
            await session.execute(update(NewCommand).where(NewCommand.user_id == user_id).values(phone_number=phone_number))
