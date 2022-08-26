from typing import AsyncGenerator

from app import application
from models import Expenses


async def get_many_by_id(user_id: int) -> AsyncGenerator[Expenses, None]:
    await application.db_connect()
    cursor = await application.get_db_cursor()
    await cursor.execute(f"SELECT ex.amount, ex.created, ca.name FROM expense AS ex, category AS ca WHERE ex.category_id=ca.id AND owner={user_id};")

    data: list[tuple] = await cursor.fetchall()
    #print('Debug ---> ', data)
    #cursor.close()

    for record in data:
        yield Expenses.from_row(record)