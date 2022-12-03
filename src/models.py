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

class Categories(BaseModel):
    category: str

    @classmethod
    def from_row(cls, row: tuple):
        return Categories(
                category=row[0],
                )

    def get_category(self):
        return self.category

