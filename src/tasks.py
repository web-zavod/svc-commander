from cgitb import text
from repository import request_repo_psql
from models import GetExpenses

async def get_expenses(user_id: int):
    expenses: list[GetExpenses] = []

    generator = request_repo_psql.get_many_by_id(user_id)

    async for expens in generator:
        expenses.append(expens.raw_text)

    text = f"Your's expenses: {', '.join(expenses)}"

    return user_id, text
