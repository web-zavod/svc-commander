from typing import AsyncGenerator

from aiopg.connection import Cursor

from models import ExpensesNames 

async def get_expense_list_by_id(cursor: Cursor, user_id: int):
    await cursor.execute(f"SELECT ca.name FROM expense AS ex JOIN category AS ca ON (ex.category_id=ca.id AND owner=%s);", (user_id, ))

    ca_name: list[tuple] = await cursor.fetchall()

    for record in ca_name:
        yield ExpensesNames.from_row(record)


async def add_expense_by_id(cursor: Cursor, user_id: int, text: str):
    ca_name_list: list[str] = []
    ca_name = get_expense_list_by_id(cursor, user_id)

    async for ca in ca_name:
        ca_name_list.append(ca.get_name())

    for ca in ca_name_list:
        if text.split(' ')[0] == ca:
            await cursor.execute(f"INSERT INTO ")
