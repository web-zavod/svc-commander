from botapi.command.v1.command_service_pb2 import ReplyMessage, IncomingMessage
from botapi.command.v1.command_service_pb2_grpc import CommandServiceServicer

from tasks import list_expenses


class CommandService(CommandServiceServicer):
    async def GetReply(self, request: IncomingMessage, context) -> ReplyMessage:
        if request.text == '/list':
            #answ = 
            async for record in list_expenses():
                str = f'Стоимость:{record[0]}, Покупка: {record[1]}'
                return ReplyMessage(user_id=request.user_id, text=str)
        else:
            return ReplyMessage(user_id=request.user_id, text=request.text)