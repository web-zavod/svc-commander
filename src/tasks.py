from repository import expenses_psql

from __main__ import application

async def get_expenses(user_id: int):
    expenses_summary: list[str] = []

    cursor = await application.get_db_cursor()

    expenses = expenses_psql.get_many_by_id(cursor, user_id)

    async for expense in expenses:    
        expenses_summary.append(expense.get_info())

    cursor.close()

    text = f'Your expenses for today:{{newline}} { "{{newline}}".join(expenses_summary)} '
        
    return user_id, text
