"""
Main Azure Functions App
Centralized function registration and routing
"""
import azure.functions as func
from utils.logger import get_logger

# Import module route registration functions
from modules.test_functions import register_routes as register_test_routes
from modules.cite_functions import register_routes as register_cite_routes

# Initialize main app logger
logger = get_logger('MainApp')

app = func.FunctionApp()

# ============= MODULE ROUTE REGISTRATION =============
logger.info('MainApp: Starting route registration')

# Register TestFunctions routes
register_test_routes(app)

# Register CiteFunctions routes
register_cite_routes(app)

logger.info('MainApp: All routes registered successfully')

