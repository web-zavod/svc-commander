from repository import expenses_psql, category_psql
from datetime import datetime

from __main__ import application
from models import Expenses


# Return user`s expense list
async def get_expenses(user_id: int):
    expenses_summary: list[tuple] = []
    user_expenses: list[str] = []

    cursor = await application.get_db_cursor()

    expenses = expenses_psql.get_many_by_id(cursor, user_id)

    # Add to list naked expense from db
    async for expense in expenses:    
        expenses_summary.append(expense.get_info())
    
    # Tale expense from list
    for expense in expenses_summary:
        # Find category by category_id from expense
        category = await category_psql.get_category_by_id(cursor, expense[2])
        # Add srt 'expense + category_name' to list
        user_expenses.append(category.get_category(expense[0], expense[1]))

    cursor.close()

    text = f'Your expenses for today:{{newline}} { "{{newline}}".join(user_expenses)} '
        
    return user_id, text

# Add new user`s expense
async def add_expenses(user_id: int, text: str):
    category_id: int
    text_list: list[str] = []
   
    # Separate text on category and expense
    for st in text.split():
        text_list.append(st)

    print('text_list =======> ', text_list)

    if len(text_list) == 2 :
        enter_category = text_list[0]
        enter_amount = text_list[1]
        try: 
            amount = int(enter_amount)
        except ValueError:
            return user_id, 'Please enter expense and amount. Ex: << кофе 200 >>'
    else:
        return user_id, 'Please enter expense and amount. Ex: << кофе 200 >>'
    
    cursor = await application.get_db_cursor()

    # Make category id for enter_category
    category = await category_psql.find_category_by_name(cursor, enter_category)
    category_id = category.get_category_id()
    
    print('expenses_names =======> ', category_id)
    
    # Add expense
    new_expense = Expenses.from_row((1, amount, datetime.now(), category_id,
                                     enter_category, user_id))
    await expenses_psql.add_expense_by_id(cursor, new_expense)
 
    cursor.close()

    return user_id, text
