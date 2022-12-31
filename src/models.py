from datetime import datetime

from pydantic import BaseModel


class Expenses(BaseModel):
    id: int
    amount: int 
    created: datetime
    category_id: int
    raw_text: str
    owner: int

    @classmethod
    def from_row(cls, row: tuple):
        return Expenses(
            id=row[0],
            amount=row[1],
            created=row[2],
            category_id=row[3],
            raw_text=row[4],
            owner=row[5],
            )

    def get_info(self):
        #return f"{self.amount} on {self.name} {self.created.strftime('%H:%M %d.%b.%Y')}"
        return self.amount, self.created.strftime('%H:%M %d.%b.%Y'), \
                self.category_id

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

    def get_category_name(self, amount: int, created: int):
        return f"{amount} on {self.name} {created}"
        #return self.name

    def get_category(self):
        return self.id, self.name, self.is_base_expense, self.aliases


