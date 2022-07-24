from pydantic import BaseModel

from app import application

"""class GetExpensesResponse(BaseModel):
    amount: int
    raw_text: str

    @classmethod
    def from_row(cls, row: tuple):
        return GetExpensesResponse(
            amount=row[0],
            raw_text=row[2],
        )"""


async def list_expenses():
    await application.db_connect()
    cursor = await application.get_db_cursor()
    await cursor.execute("SELECT amount, raw_text FROM expense")
        
    data: list[tuple] = await cursor.fetchall()
    
    yield data

#    for record in data:
#        yield GetExpensesResponse.from_row(record)
