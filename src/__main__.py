import asyncio
import logging
from typing import NoReturn, Optional

from .app import application 
from .logger import setup_logger
from services import HealthcheckService, CommandService
from settings import AppSettings


settings=AppSettings.load()

main_logger = logging.getLogger(__name__)
setup_logger()


async def main() -> Optional[NoReturn]:

    # HealthCheck Service
    main_logger.info('Adding gRPC services...')
    await application.add_service(
            HealthcheckService,
            "healthcheck",
            "1",
            )
    # Command Service
    await application.add_service(
            CommandService,
            "command",
            "1",
            )

    try:
        await application.db_connect()
        await application.run()
    except Exception as err:
        await application.db_disconnect()
        main_logger.info(f"Error running app: {str(err)}")
        raise

loop = asyncio.get_event_loop()

try:
    loop.run_until_complete(main())
finally:
    pending = asyncio.all_tasks(loop)

    if pending:
        loop.run_until_complete(asyncio.gather(*pending))

    main_logger.debug('Closing the event loop...')
    loop.close()
