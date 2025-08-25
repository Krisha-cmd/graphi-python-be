"""
Custom logger utility for Azure Functions
Provides standardized logging across all modules
"""
import logging
import sys
from datetime import datetime
from typing import Optional


class CustomLogger:
    """Custom logger class for Azure Functions with enhanced formatting"""
    
    def __init__(self, name: str, level: int = logging.INFO):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)
        
        # Avoid duplicate handlers
        if not self.logger.handlers:
            self._setup_handler()
    
    def _setup_handler(self):
        """Setup console handler with custom formatting"""
        handler = logging.StreamHandler(sys.stdout)
        handler.setLevel(logging.INFO)
        
        # Custom formatter
        formatter = logging.Formatter(
            fmt='%(asctime)s - [%(name)s] - %(levelname)s - %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)
    
    def info(self, message: str, extra_data: Optional[dict] = None):
        """Log info message with optional extra data"""
        if extra_data:
            message = f"{message} | Data: {extra_data}"
        self.logger.info(message)
    
    def error(self, message: str, exception: Optional[Exception] = None, extra_data: Optional[dict] = None):
        """Log error message with optional exception and extra data"""
        if exception:
            message = f"{message} | Exception: {str(exception)}"
        if extra_data:
            message = f"{message} | Data: {extra_data}"
        self.logger.error(message)
    
    def warning(self, message: str, extra_data: Optional[dict] = None):
        """Log warning message with optional extra data"""
        if extra_data:
            message = f"{message} | Data: {extra_data}"
        self.logger.warning(message)
    
    def debug(self, message: str, extra_data: Optional[dict] = None):
        """Log debug message with optional extra data"""
        if extra_data:
            message = f"{message} | Data: {extra_data}"
        self.logger.debug(message)


def get_logger(module_name: str) -> CustomLogger:
    """
    Get a logger instance for a specific module
    
    Args:
        module_name: Name of the module (e.g., 'TestFunctions', 'CiteFunctions')
    
    Returns:
        CustomLogger instance
    """
    return CustomLogger(module_name)
