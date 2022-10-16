from repository import request_repo_psql

async def get_expenses(user_id: int):
    expenses: list[str] = []

    generator = request_repo_psql.get_many_by_id(user_id)

    async for expense in generator:    
        expenses.append(expense.get_info())

    text = 'Your expenses for today:{{newline}} {0}'.format("{{newline}}".join(expenses))
    
    return user_id, text
