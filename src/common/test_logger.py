from logger import get_logger

logger = get_logger(__name__)

logger.info("Application started.")
logger.info("Logger initialized successfully.")
logger.warning("This is a sample warning.")
logger.error("This is a sample error.")