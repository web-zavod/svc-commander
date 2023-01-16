from typing import AsyncGenerator

from aiopg.connection import Cursor

from models import Expense


class ExpenseRepository:
    @classmethod
    async def get_many_by_id(cls, cursor: Cursor, user_id: int) -> AsyncGenerator[Expense, None]:
        await cursor.execute(
                "SELECT ex.amount, ex.created, ex.category_id, ca.name, ex.owner " + 
                "FROM expense AS ex " + 
                "JOIN category AS ca ON (ex.category_id=ca.id AND owner=%s);", (user_id, ) )

        data: list[tuple] = await cursor.fetchall()

        for record in data:
            yield Expense.from_row(record)

    @classmethod
    async def add_by_id(cls, cursor: Cursor, add_ex):
        print(add_ex.amount, add_ex.category_id, add_ex.category_name, add_ex.owner)
        await cursor.execute(
                "INSERT INTO expense (amount, category_id, raw_text, owner) " + 
                "VALUES (%s, %s, %s, %s);",
                (add_ex.amount, add_ex.category_id, add_ex.category_name, add_ex.owner, ))

