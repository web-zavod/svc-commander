import asyncio
import logging
from typing import NoReturn, Optional

from .app import Application
from .logger import setup_logger
from services import HealthcheckService, CommandService
from settings import AppSettings


settings=AppSettings.load()

main_logger = logging.getLogger(__name__)
setup_logger()


async def main() -> Optional[NoReturn]:
    app = Application(settings=settings)

    # HealthCheck Service
    main_logger.info('Adding gRPC services...')
    await app.add_service(
            HealthcheckService,
            "healthcheck",
            "1",
            )
    # Command Service
    await app.add_service(
            CommandService,
            "command",
            "1",
            )

    try:
        await app.run()
    except Exception as err:
        main_logger.info(f"Error running app: {str(err)}")
        raise

loop = asyncio.new_event_loop()

try:
    loop.run_until_complete(main())
finally:
    pending = asyncio.all_tasks(loop)

    if pending:
        loop.run_until_complete(asyncio.gather(*pending))

    main_logger.debug('Closing the event loop...')
    loop.close()