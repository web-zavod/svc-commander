from repository import expenses_psql, category_psql
from datetime import datetime

from __main__ import application
from models import Expense


async def get_expenses(user_id: int) -> tuple[int, str]:
    expenses_summary: list[str] = []

    cursor = await application.get_db_cursor()

    expenses = expenses_psql.ExpenseRepository.get_many_by_id(cursor, user_id)

    async for expense in expenses:    
        expenses_summary.append(expense.get_info())

    cursor.close()

    text = f'Your expenses for today:{{newline}} { "{{newline}}".join(expenses_summary)} '
        
    return user_id, text

async def add_expenses(user_id: int, text: str) -> tuple[int, str]:
    match text.split():
        case [category, amount]:
            try: 
                enter_category: str = str(category)
                enter_amount: int = int(amount)
            except ValueError:
                return user_id, 'Please enter expense and amount. Ex: << кофе 200 >>'
        case _:
            return user_id, 'Please enter expense and amount. Ex: << кофе 200 >>'

    cursor = await application.get_db_cursor()

    category = await category_psql.CategoryRepository.find_by_name(cursor, enter_category)

    print('time =======> ',datetime.today())

    expense = Expense(amount= enter_amount,
            created = datetime.today(),
            category_id = category.id,
            category_name = enter_category,
            owner = user_id 
                      )
    await expenses_psql.ExpenseRepository.add_by_id(cursor, expense)

    cursor.close()

    return user_id, text
