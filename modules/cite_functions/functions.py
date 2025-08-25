"""
CiteFunctions module
Contains all citation-related Azure Functions
"""
import json
import azure.functions as func
from utils.logger import get_logger

# Initialize logger for this module
logger = get_logger('CiteFunctions')

