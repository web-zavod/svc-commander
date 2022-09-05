from cgitb import text
from repository import request_repo_psql
from models import Expenses

async def get_expenses(user_id: int):
    expenses: list[str] = []

    generator = request_repo_psql.get_many_by_id(user_id)

    async for expens in generator:    
        #print('debug ---> ', expens.get_info())
        expenses.append(expens.get_info())

    text = 'Your expenses for today:[newline] {0}'.format("[newline]".join(expenses))
    
    return user_id, text
