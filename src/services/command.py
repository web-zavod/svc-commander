from botapi.command.v1.command_service_pb2 import ReplyMessage, IncomingMessage
from botapi.command.v1.command_service_pb2_grpc import CommandServiceServicer

from tasks import get_expenses, categories_list

class CommandService(CommandServiceServicer):
    async def GetReply(self, request: IncomingMessage, context) -> ReplyMessage:
        if request.text == '/list':
            user_id, text= await get_expenses(request.user_id)
            return ReplyMessage(user_id=user_id, text=text)
        elif request.text == '/category':
            user_id, text = await categories_list(request.user_id)
            return ReplyMessage(user_id=user_id, text=text)
        else:
            return ReplyMessage(user_id=request.user_id, text=request.text)

        
