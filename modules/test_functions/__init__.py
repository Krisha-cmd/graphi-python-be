"""
TestFunctions module
Contains all test-related Azure Functions
"""
import azure.functions as func
from utils.logger import get_logger
from .functions import hello_test_function

# Initialize logger for route registration
logger = get_logger('TestFunctions.Routes')


def register_routes(app: func.FunctionApp):
    """
    Register all TestFunctions routes with the main app
    
    Args:
        app: The main Azure Functions app instance
    """
    logger.info('TestFunctions: Registering routes')
    
    @app.route(route="test/hello", auth_level=func.AuthLevel.ANONYMOUS)
    def HelloTestFunction(req: func.HttpRequest) -> func.HttpResponse:
        """Test module: Hello function"""
        logger.info('TestFunctions: HelloTest route accessed')
        return hello_test_function(req)
    
    logger.info('TestFunctions: Routes registered successfully')
