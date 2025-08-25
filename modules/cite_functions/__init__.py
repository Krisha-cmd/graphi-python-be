"""
CiteFunctions module
Contains all citation-related Azure Functions
"""
import azure.functions as func
from utils.logger import get_logger

# Initialize logger for route registration
logger = get_logger('CiteFunctions.Routes')


def register_routes(app: func.FunctionApp):
    """
    Register all CiteFunctions routes with the main app
    
    Args:
        app: The main Azure Functions app instance
    """
    logger.info('CiteFunctions: Registering routes')
    
    logger.info('CiteFunctions: Routes registered successfully')
