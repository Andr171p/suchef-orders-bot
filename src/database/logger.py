import logging


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(messages)s',
    level=logging.INFO
)

logger = logging.getLogger(
    name="database-service"
)
