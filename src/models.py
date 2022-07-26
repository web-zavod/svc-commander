from pydantic import BaseModel


class GetExpensesInfo(BaseModel):
    amount: int 
    raw_text: str

    @classmethod
    def from_row(cls, row: tuple):
        return GetExpensesInfo(
            amount=row[0],
            raw_text=row[1],
            )