from typing import AsyncGenerator
from pydantic import BaseModel

from app import application
from models import GetExpensesInfo


async def list_expenses() -> AsyncGenerator[GetExpensesInfo, None]:
    await application.db_connect()
    cursor = await application.get_db_cursor()
    await cursor.execute("SELECT amount, raw_text FROM expense")
        
    data: list[tuple] = await cursor.fetchall()

    for record in data:
        yield GetExpensesInfo.from_row(record)