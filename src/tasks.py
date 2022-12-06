from repository import expenses_psql, add_expenses_psql

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


async def add_expenses(user_id: int, text: str):
    cursor = await application.get_db_cursor()
    
    if await add_expenses_psql.add_expense_by_id(cursor, user_id, text):
        text = f'Add expenses: {text}'
    else:
        print ('Err -- > Can`t add expense')

    cursor.close()


    return user_id, text
