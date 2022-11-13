from typing import AsyncGenerator

from aiopg.connection import Cursor

from models import Expenses

async def get_many_by_id(cursor: Cursor, user_id: int) -> AsyncGenerator[Expenses, None]:
    await cursor.execute(f"SELECT ex.amount, ex.created, ca.name FROM expense AS ex JOIN category AS ca ON (ex.category_id=ca.id AND owner=%s);", (user_id, ) )

    data: list[tuple] = await cursor.fetchall()

    for record in data:
        yield Expenses.from_row(record)
