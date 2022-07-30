from repository import request_repo_psql

async def get_expenses():
    async for ans in request_repo_psql.list_expenses():
        return f"Cost: {ans.amount} \n Type: {ans.raw_text}"
