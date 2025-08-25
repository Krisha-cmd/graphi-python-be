"""
TestFunctions module
Contains all test-related Azure Functions
"""
import json
import azure.functions as func
from utils.logger import get_logger

# Initialize logger for this module
logger = get_logger('TestFunctions')


def hello_test_function(req: func.HttpRequest) -> func.HttpResponse:
    """
    Test function to demonstrate module structure
    Moved from the main function_app.py
    """
    logger.info('TestFunctions: HelloTest function processed a request')

    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            logger.warning('TestFunctions: Invalid JSON in request body')
            pass
        else:
            name = req_body.get('name') if req_body else None

    if name:
        response_message = f"Hello, {name}. This TEST function executed successfully."
        logger.info('TestFunctions: Successful response generated', {'name': name})
        return func.HttpResponse(response_message)
    else:
        response_message = "This TEST function executed successfully. Pass a name in the query string or in the request body for a personalized response."
        logger.info('TestFunctions: Default response generated')
        return func.HttpResponse(response_message, status_code=200)


