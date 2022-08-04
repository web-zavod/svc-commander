from pydantic import BaseModel


class GetExpenses(BaseModel):
    amount: int 
    created: str
    category_id: int
    raw_text: str
    user_id: int

    @classmethod
    def from_row(cls, row: tuple):
        return GetExpenses(
            amount=row[0],
            created=row[1],
            category_id=row[2],
            raw_text=row[3],
            user_id=row[4],
            )
