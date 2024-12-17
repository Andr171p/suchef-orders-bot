import logging


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(text)s',
    level=logging.INFO
)

logger = logging.getLogger(
    name="database-service"
)
