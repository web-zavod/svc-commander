from typing import AsyncGenerator
from pydantic import BaseModel

from botapi.command.v1.command_service_pb2 import IncomingMessage

from app import application
from models import GetExpensesInfo


async def list_expenses() -> AsyncGenerator[GetExpensesInfo, None]:
    user_id: int = IncomingMessage()
    await application.db_connect()
    cursor = await application.get_db_cursor()
    await cursor.execute(f"SELECT * FROM expense WHERE owner={user_id.user_id};")
    
    data: list[tuple] = await cursor.fetchall()

    application.db_disconnect()

    for record in data:
        yield GetExpensesInfo.from_row(record)