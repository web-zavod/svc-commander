from datetime import datetime

from pydantic import BaseModel


class Expense(BaseModel):
    amount: int 
    created: datetime
    category_id: int
    category_name: str
    owner: int

    @classmethod
    def from_row(cls, row: tuple):
        return Expense(
            amount=row[0],
            created=row[1],
            category_id=row[2],
            category_name=row[3],
            owner=row[4],
            )

    def get_info(self) -> str:
        return f"{self.amount} on {self.category_name} {self.created.strftime('%H:%M %d.%b.%Y')}"


class Category(BaseModel):
    id: int
    name: str
    is_base_expense: bool
    aliases: str

    @classmethod
    def from_row(cls, row: tuple):
        return Category(
                id=row[0],
                name=row[1],
                is_base_expense=row[2],
                aliases=row[3],
                )

