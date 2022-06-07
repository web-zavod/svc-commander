import re
from botapi.command.v1.command_service_pb2 import ReplyMessage
from botapi.command.v1.command_service_pb2_grpc import CommandServiceServicer

class CommandService(CommandServiceServicer):
    async def GetReply(self, request, context):
        return ReplyMessage(user_id= request.user_id, text= request.text)