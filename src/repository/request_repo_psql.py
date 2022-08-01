from typing import AsyncGenerator

from app import application
from models import GetExpensesInfo


async def list_expenses(user_id: int) -> AsyncGenerator[GetExpensesInfo, None]:
    await application.db_connect()
    cursor = await application.get_db_cursor()
    await cursor.execute(f"SELECT * FROM expense WHERE owner={user_id};")
    
    data: list[tuple] = await cursor.fetchall()

    application.db_disconnect()

    for record in data:
        yield GetExpensesInfo.from_row(record)