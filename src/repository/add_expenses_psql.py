from typing import AsyncGenerator

from aiopg import Cursor

async def add_expenses(cursor: Cursor, user_id: int):
    await cursor.execute(f"")
