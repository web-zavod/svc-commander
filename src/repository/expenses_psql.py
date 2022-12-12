from typing import AsyncGenerator

from aiopg.connection import Cursor

from models import Expenses, ExpensesNames

async def get_many_by_id(cursor: Cursor, user_id: int) -> AsyncGenerator[Expenses, None]:
    await cursor.execute(f"SELECT ex.amount, ex.created, ca.name FROM expense AS ex JOIN category AS ca ON (ex.category_id=ca.id AND owner=%s);", (user_id, ) )

    data: list[tuple] = await cursor.fetchall()

    for record in data:
        yield Expenses.from_row(record)

async def get_category_by_id(cursor: Cursor, user_id:int):
    #await cursor.execute(f"SELECT ca.name FROM category AS ca JOIN expense AS ex ON (ex.category_id=ca.id AND owner=%s);", (user_id, ))
    await cursor.execute("SELECT ca.id, ca.name FROM category AS ca LEFT JOIN expense AS ex ON (ex.category_id=ca.id AND ex.owner=%s);", (user_id, ))

    data: list[tuple] = await cursor.fetchall()

    for record in data:
        yield ExpensesNames.from_row(record)

async def add_expense_by_id(cursor: Cursor, user_id: int, category: str, amount: int, category_id: int):
    #await cursor.execute(f"INSERT INTO expense SELECT amount FROM expense JOIN category AS ca ON (expense.category_id=ca.id AND amount=%s AND ca.name=%s AND owner=%s);", (amount, category, user_id, ))
    await cursor.execute("INSERT INTO expense (amount, category_id, raw_text, owner) VALUES (%s, %s, %s, %s);", (amount, category_id, category, user_id, ))


