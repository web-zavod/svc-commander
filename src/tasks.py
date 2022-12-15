from repository import expenses_psql, category_psql

from __main__ import application
from models import AddExpense

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
    expenses_names: list[tuple] = []
    text_list: list[str] = []
    
    for st in text.split():
        text_list.append(st)

    print('text_list =======> ', text_list)

    if len(text_list) == 2 :
        category = text_list[0]
        amount = text_list[1]
        try: 
            amount = int(amount)
        except ValueError:
            return user_id, 'Please enter expense and amount. Ex: << кофе 200 >>'
    else:
        return user_id, 'Please enter expense and amount. Ex: << кофе 200 >>'
    
    cursor = await application.get_db_cursor()

    expenses = category_psql.find_category_by_name(cursor, category)
    
    async for expense in expenses:
        expenses_names.append(expense.get_category())
    
    print('expenses_names =======> ', expenses_names)

    add_ex = AddExpense(amount=amount, category_id=expenses_names[0][0], raw_text=category, owner=user_id,   )

    await expenses_psql.add_expense_by_id(cursor, add_ex)
 
    cursor.close()

    return user_id, text
