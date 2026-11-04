"""
TASE-Database bot service.

Minimal placeholder implementation that runs continuously and logs a
heartbeat message periodically, demonstrating a 24/7 running service on
Railway. Replace the body of `run()` with the actual database bot logic.
"""

import logging
import signal
import sys
import time

LOG_INTERVAL_SECONDS = 300  # 5 minutes

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    stream=sys.stdout,
)

logger = logging.getLogger("tase-database")

_running = True


def _handle_shutdown(signum, frame):
    global _running
    logger.info("Received signal %s, shutting down gracefully...", signum)
    _running = False


def run():
    logger.info("TASE-Database bot starting up...")

    signal.signal(signal.SIGTERM, _handle_shutdown)
    signal.signal(signal.SIGINT, _handle_shutdown)

    iteration = 0
    while _running:
        iteration += 1
        logger.info("Bot is alive - heartbeat #%d", iteration)

        # TODO: Replace this placeholder with the actual bot logic
        # (e.g., fetching data, updating the database, etc.)

        for _ in range(LOG_INTERVAL_SECONDS):
            if not _running:
                break
            time.sleep(1)

    logger.info("TASE-Database bot stopped.")


if __name__ == "__main__":
    run()
