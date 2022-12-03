from typing import AsyncGenerator

from aiopg.connection import Cursor

from models import Categories

async def get_category_by_id(cursor: Cursor, user_id: int) -> AsyncGenerator[Categories, None]:
    await cursor.execute(f"SELECT ca.name FROM category AS ca JOIN expense AS ex ON (ca.id=ex.category_id AND ex.owner=%s);", (user_id))

    data: list[tuple] = await cursor.fetchall()

    for record in data:
        yield Categories.from_row(record)
