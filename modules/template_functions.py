"""
TEMPLATE: New Module Structure
This is a template showing how to create a new module with self-contained routing.

For a new module, create:
1. modules/your_module_name/__init__.py (with register_routes function)
2. modules/your_module_name/functions.py (with actual function implementations)

Copy this template to modules/your_module_name/__init__.py and modify as needed.
"""
import azure.functions as func
from utils.logger import get_logger
from .functions import your_function_name, another_function_name  # Import your actual functions

# Initialize logger for route registration
logger = get_logger('YourModuleName.Routes')


def register_routes(app: func.FunctionApp):
    """
    Register all YourModuleName routes with the main app
    
    Args:
        app: The main Azure Functions app instance
    """
    logger.info('YourModuleName: Registering routes')
    
    @app.route(route="your-module/endpoint1", auth_level=func.AuthLevel.ANONYMOUS)
    def YourFunction1(req: func.HttpRequest) -> func.HttpResponse:
        """Your module: Description of function 1"""
        logger.info('YourModuleName: Function1 route accessed')
        return your_function_name(req)

    @app.route(route="your-module/endpoint2", auth_level=func.AuthLevel.ANONYMOUS)
    def YourFunction2(req: func.HttpRequest) -> func.HttpResponse:
        """Your module: Description of function 2"""
        logger.info('YourModuleName: Function2 route accessed')
        return another_function_name(req)
    
    logger.info('YourModuleName: Routes registered successfully')


# This template should be renamed to __init__.py in your actual module directory
