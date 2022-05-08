"""Healthcheck service"""
__all__ = ["HealthcheckService"]

import logging
import grpc
from google.protobuf.empty_pb2 import Empty

from botapi.healthcheck.v1.healthcheck_service_pb2 import CheckResponse
from botapi.healthcheck.v1.healthcheck_service_pb2_grpc import HealthcheckServiceServicer

logger = logging.getLogger(__name__)

class HealthcheckService(HealthcheckServiceServicer):
    async def Check(
            self,
            request: Empty,
            context: grpc.ServicerContext,
            ):
        """Method to check health of service"""
        logger.info("Healthcheck call")
        return CheckResponse(message="Ok!")