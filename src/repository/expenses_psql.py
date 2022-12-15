from typing import AsyncGenerator

from aiopg.connection import Cursor

from models import Expenses, AddExpense

async def get_many_by_id(cursor: Cursor, user_id: int) -> AsyncGenerator[Expenses, None]:
    await cursor.execute(f"SELECT ex.amount, ex.created, ca.name FROM expense AS ex JOIN category AS ca ON (ex.category_id=ca.id AND owner=%s);", (user_id, ) )

    data: list[tuple] = await cursor.fetchall()

    for record in data:
        yield Expenses.from_row(record)


async def add_expense_by_id(cursor: Cursor, add_ex: AddExpense):
    await cursor.execute("INSERT INTO expense (amount, category_id, raw_text, owner) VALUES (%s, %s, %s, %s);",\
            (add_ex.amount, add_ex.category_id, add_ex.raw_text, add_ex.owner, ))


