from sqlalchemy import select
from sqlalchemy.orm import sessionmaker

from database.create_table import NewPlayer, NewCommand


async def count_ids(session_maker: sessionmaker):
    async with session_maker() as session:
        async with session.begin():
            result = await session.execute(select(NewPlayer.id_))
            count_ids = [row[0] for row in result.all()]
            return count_ids


async def count_user_id(session_maker: sessionmaker):
    async with session_maker() as session:
        async with session.begin():
            result = await session.execute(select(NewPlayer.user_id))
            user_id = [row[0] for row in result.all()]
            return user_id


async def count_fill_name(session_maker: sessionmaker):
    async with session_maker() as session:
        async with session.begin():
            result = await session.execute(select(NewPlayer.full_name))
            names = [row[0] for row in result]
            return names


async def count_birthday(session_maker: sessionmaker):
    async with session_maker() as session:
        async with session.begin():
            result = await session.execute(select(NewPlayer.birthday))
            birthday = [row[0] for row in result]
            return birthday


async def count_stick_grip(session_maker: sessionmaker):
    async with session_maker() as session:
        async with session.begin():
            result = await session.execute(select(NewPlayer.stick_grip))
            stick_grip = [row[0] for row in result]
            return stick_grip


async def count_photo(session_maker: sessionmaker):
    async with session_maker() as session:
        async with session.begin():
            result = await session.execute(select(NewPlayer.photo))
            photo = [row[0] for row in result]
            return photo


async def delete_player(session_maker, user_id):
    async with session_maker() as session:
        async with session.begin():
            records_to_delete = await session.execute(select(NewPlayer).where(NewPlayer.user_id == user_id))

            for record in records_to_delete:
                session.delete(record)


async def count_name(session_maker: sessionmaker):
    async with session_maker() as session:
        async with session.begin():
            result = await session.execute(select(NewCommand.name))
            names = [row[0] for row in result]
            return names


async def count_foundation(session_maker: sessionmaker):
    async with session_maker() as session:
        async with session.begin():
            result = await session.execute(select(NewCommand.foundation))
            foundation = [row[0] for row in result]
            return foundation


async def count_arena(session_maker: sessionmaker):
    async with session_maker() as session:
        async with session.begin():
            result = await session.execute(select(NewCommand.arena))
            arena = [row[0] for row in result]
            return arena


async def count_contact(session_maker: sessionmaker):
    async with session_maker() as session:
        async with session.begin():
            result = await session.execute(select(NewCommand.contact))
            contact = [row[0] for row in result]
            return contact


async def count_number(session_maker: sessionmaker):
    async with session_maker() as session:
        async with session.begin():
            result = await session.execute(select(NewCommand.phone_number))
            number = [row[0] for row in result]
            return number
