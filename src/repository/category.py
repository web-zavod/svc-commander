from typing import AsyncGenerator

from aiopg.connection import Cursor

from models import Category


class CategoryRepository:
    @classmethod
    async def find_by_name(cls, cursor: Cursor, name: str) -> Category:
        await cursor.execute(
                            "SELECT * FROM category AS ca WHERE (ca.name=%s);",
                            (name, )
                            )

        data: list[tuple] = await cursor.fetchall()

        if len(data) == 0:
            await cursor.execute(
                                "SELECT * FROM category AS ca WHERE (ca.name='прочее');"
                                )

            data: list[tuple] = await cursor.fetchall()

        return Category.from_row(data[0])

