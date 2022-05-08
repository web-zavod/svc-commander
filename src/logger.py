"""Application logger setup"""

__all__ = ['setup_logger']

import logging
import sys
from enum import Enum

class Level(str, Enum):
    """Enum of available logger levels"""
    DEBUG = logging.getLevelName(logging.DEBUG)
    INFO = logging.getLevelName(logging.INFO)
    WARNING = logging.getLevelName(logging.WARNING)
    ERROR = logging.getLevelName(logging.ERROR)
    FATAL = logging.getLevelName(logging.FATAL)

def setup_logger() -> None:
    """Set a logger stream output, its level and a message format"""
    logging.basicConfig(
        stream=sys.stdout,
        level=Level.DEBUG.value,
        format='%(asctime)s - [%(name)s] - [%(levelname)s]: %(message)s',
    )
