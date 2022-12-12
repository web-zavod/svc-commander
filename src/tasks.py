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

    expenses = expenses_psql.get_category_by_id(cursor, user_id)
    
    async for expense in expenses:
        expenses_names.append(expense.get_name())
    
    print('expenses_names =======> ', expenses_names)

    names: list[str] = []
    for name in expenses_names:
        names.append(name[1])

    if category in names:
        for ca_id in expenses_names:
            if category == ca_id[1]:
                category_id = ca_id[0]
                await expenses_psql.add_expense_by_id(cursor, user_id, category, amount, category_id)
    else:
        category_id = 11
        await expenses_psql.add_expense_by_id(cursor, user_id, 'прочее', amount, category_id)
 
    cursor.close()

    return user_id, text
