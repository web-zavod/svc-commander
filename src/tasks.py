from repository import expenses_psql

async def get_expenses(user_id: int):
    expenses: list[str] = []

    generator = expenses_psql.get_many_by_id(user_id)

    async for expense in generator:    
        expenses.append(expense.get_info())

    text = f'Your expenses for today:{{newline}} { "{{newline}}".join(expenses)} '
    
    return user_id, text
