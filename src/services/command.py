from botapi.command.v1.command_service_pb2 import ReplyMessage, IncomingMessage
from botapi.command.v1.command_service_pb2_grpc import CommandServiceServicer

from tasks import get_expenses


class CommandService(CommandServiceServicer):
    async def GetReply(self, request: IncomingMessage, context) -> ReplyMessage:
        if request.text == '/list':
            return ReplyMessage(user_id=request.user_id, text=get_expenses())
        else:
            return ReplyMessage(user_id=request.user_id, text=request.text)