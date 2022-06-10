import logging
from botapi.command.v1.command_service_pb2 import ReplyMessage, IncomingMessage
from botapi.command.v1.command_service_pb2_grpc import CommandServiceServicer

logger = logging.getLogger(__name__)

class CommandService(CommandServiceServicer):
    async def GetReply(self, request: IncomingMessage, context) -> ReplyMessage:
        logger.debug(f"Receive command: user_id={request.user_id}, text={request.text}")
        return ReplyMessage(user_id=request.user_id, text=request.text)