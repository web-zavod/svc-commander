from typing import AsyncGenerator

from app import application
from models import GetExpenses


async def get_many_by_id(user_id: int) -> AsyncGenerator[GetExpenses, None]:
    await application.db_connect()
    cursor = await application.get_db_cursor()
    await cursor.execute(f"SELECT * FROM expense WHERE owner={user_id};")
    
    data: list[tuple] = await cursor.fetchall()

    cursor.close()

    for record in data:
        yield GetExpenses.from_row(record)