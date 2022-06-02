from botapi.command.v1.command_service_pb2 import ReplyMessage
from botapi.command.v1.command_service_pb2_grpc import CommandServiceServicer

class CommandService(CommandServiceServicer):
    async def GetReply(self, request, context):
        print(dir(request))
        print(dir(context))
        return ReplyMessage()