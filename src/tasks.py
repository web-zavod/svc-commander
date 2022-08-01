from ast import In
from botapi.command.v1.command_service_pb2 import IncomingMessage

from repository import request_repo_psql

async def get_expenses(id: IncomingMessage):
    async for ans in request_repo_psql.list_expenses(id.user_id):
        return f"Cost: {ans.amount} \n Type: {ans.raw_text}"
