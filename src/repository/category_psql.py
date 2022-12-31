from typing import AsyncGenerator

from aiopg.connection import Cursor

from models import Category


async def get_category_by_id(cursor: Cursor, category_id: int):
    await cursor.execute(
            "SELECT * FROM category WHERE category.id=%s;", (category_id, )
            )
    data: list[tuple] = await cursor.fetchall()

    return Category.from_row(data[0])

async def find_category_by_name(cursor: Cursor, category_name: str):
    await cursor.execute(
                        "SELECT * FROM category AS ca WHERE (ca.name=%s) OR (ca.name='прочее');",\
                        (category_name, )
                        )

    data: list[tuple] = await cursor.fetchall()

    for record in data:
        yield Category.from_row(record)

