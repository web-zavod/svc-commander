from datetime import datetime

from pydantic import BaseModel


class Expenses(BaseModel):
    amount: int 
    created: datetime
    name: str

    @classmethod
    def from_row(cls, row: tuple):
        return Expenses(
            amount=row[0],
            created=row[1],
            name=row[2],
            )

    def get_info(self):
        return f"{self.amount} on {self.name} {self.created.strftime('%H:%M %d.%b.%Y')}"

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

    def get_category(self):
        return self.id, self.name, self.is_base_expense, self.aliases

class AddExpense(BaseModel):
    amount: int
    category_id: int
    raw_text: str
    owner: int

