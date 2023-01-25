from datetime import datetime, timezone

from __main__ import application
from models import Expense
from repository.expense import ExpenseRepository
from repository.category import CategoryRepository

async def get_expenses(user_id: int) -> tuple[int, str]:
    expenses_summary: list[str] = []

    cursor = await application.get_db_cursor()

    expenses = ExpenseRepository.get_many_by_id(cursor, user_id)

    async for expense in expenses:    
        expenses_summary.append(expense.get_info())

    cursor.close()

    text = f'Your expenses for today:{{newline}} { "{{newline}}".join(expenses_summary)} '
        
    return user_id, text

async def add_expense(user_id: int, text: str) -> tuple[int, str]:
    match text.split():
        case [category, amount]:
            if category.isnumeric():
                enter_category: str = str(amount)
                enter_amount: int = int(category)
            elif amount.isnumeric():
                enter_category: str = str(category)
                enter_amount: int = int(amount)
            else:
                return user_id, 'Please enter expense and amount. Ex: << кофе 200 >>'
        case _:
            return user_id, 'Please enter expense and amount. Ex: << кофе 200 >>'

    cursor = await application.get_db_cursor()

    category = await CategoryRepository.find_by_name(cursor, enter_category)

    expense = Expense(
            amount = enter_amount,
            created = datetime.now(),
            category_id = category.id,
            category_name = enter_category,
            owner = user_id 
                      )
    await ExpenseRepository.save(cursor, expense)

    cursor.close()

    return user_id, text
