# Azure Functions Project - Modular Architecture

This Azure Functions project is organized using a modular architecture to maintain code organization, reusability, and scalability.

## 📋 Documentation

- **[Main Documentation](#)** - This file (project setup, modules, coding guidelines)
- **[Branching Strategy](BRANCHING_STRATEGY.md)** - Repository management, branch conventions, and workflow

## Project Structure

```
graphi-python-be/
├── function_app.py          # Main app entry point and routing
├── host.json               # Azure Functions host configuration
├── local.settings.json     # Local development settings
├── requirements.txt        # Python dependencies
├── README.md              # This file
├── modules/               # Function modules
│   ├── __init__.py
│   ├── test_functions/    # Test-related functions
│   │   ├── __init__.py
│   │   └── functions.py
│   └── cite_functions/    # Citation-related functions
│       ├── __init__.py
│       └── functions.py
└── utils/                 # Shared utilities
    ├── __init__.py
    └── logger.py         # Custom logger
```

## Naming Conventions

### Module Naming
- **Modules**: Use `snake_case` for module directories (e.g., `test_functions`, `cite_functions`)
- **Module Files**: Use `functions.py` for the main function implementations
- **Package Files**: Always include `__init__.py` files in directories

### Function Naming
- **Function Names**: Use `snake_case` for function names (e.g., `hello_test_function`)
- **Route Functions**: Use `PascalCase` for Azure Functions route handlers (e.g., `HelloTestFunction`)
- **Route Paths**: Use lowercase with forward slashes (e.g., `"test/hello"`, `"cite/generate"`)

### Logger Naming
- Use the module name as the logger identifier (e.g., `'TestFunctions'`, `'CiteFunctions'`, `'MainApp'`)

## Adding New Modules

### Step 1: Create Module Directory Structure
```powershell
# Create the main module directory
mkdir modules\your_module_name

# Create __init__.py file
New-Item -ItemType File -Path "modules\your_module_name\__init__.py"

# Create functions.py file
New-Item -ItemType File -Path "modules\your_module_name\functions.py"
```

### Step 2: Create Module Templates
In `modules\your_module_name\__init__.py`:
```python
"""
YourModuleName module
Contains all your-feature-related Azure Functions
"""
import azure.functions as func
from utils.logger import get_logger
from .functions import your_function_name, another_function_name

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
```

In `modules\your_module_name\functions.py`:
```python
"""
YourModuleName module
Contains all your-feature-related Azure Functions
"""
import json
import azure.functions as func
from utils.logger import get_logger

# Initialize logger for this module
logger = get_logger('YourModuleName')


def your_function_name(req: func.HttpRequest) -> func.HttpResponse:
    """
    Brief description of what this function does
    """
    logger.info('YourModuleName: FunctionName function processed a request')
    
    # Your function logic here
    
    return func.HttpResponse(
        "Your response message",
        status_code=200
    )
```

### Step 3: Register Module in Main App
In `function_app.py`:
```python
# Add import at the top
from modules.your_module_name import register_routes as register_your_module_routes

# Add route registration in the module registration section
register_your_module_routes(app)
```

## Adding Functions to Existing Modules

### Step 1: Add Function to Module
In the appropriate `modules\module_name\functions.py` file:
```python
def new_function_name(req: func.HttpRequest) -> func.HttpResponse:
    """
    Description of the new function
    """
    logger.info('ModuleName: NewFunction processed a request')
    
    # Your function logic here
    
    return func.HttpResponse("Response message", status_code=200)
```

### Step 2: Update Module Routes
In `modules\module_name\__init__.py`, update the `register_routes` function:
```python
# Add import for new function
from .functions import existing_function, new_function_name

def register_routes(app: func.FunctionApp):
    """Register all ModuleName routes with the main app"""
    logger.info('ModuleName: Registering routes')
    
    # ...existing routes...
    
    # Add new route
    @app.route(route="module/new-endpoint", auth_level=func.AuthLevel.ANONYMOUS)
    def NewRouteFunction(req: func.HttpRequest) -> func.HttpResponse:
        """Module: New function description"""
        logger.info('ModuleName: NewFunction route accessed')
        return new_function_name(req)
    
    logger.info('ModuleName: Routes registered successfully')
```

**Note:** No changes needed in `function_app.py` - the module automatically registers its own routes!

## Using the Custom Logger

### Basic Usage
```python
from utils.logger import get_logger

# Initialize logger for your module
logger = get_logger('YourModuleName')

# Log different levels
logger.info('This is an info message')
logger.warning('This is a warning message')
logger.error('This is an error message')
logger.debug('This is a debug message')
```

### Advanced Usage with Extra Data
```python
# Log with extra context data
logger.info('Function processed successfully', {'user_id': '123', 'request_size': 1024})

# Log errors with exception details
try:
    # Your code here
    pass
except Exception as e:
    logger.error('Function failed', exception=e, extra_data={'context': 'additional_info'})
```

### Logger Features
- **Standardized Format**: Consistent timestamp and module identification
- **Extra Data Support**: Include contextual information in logs
- **Exception Handling**: Built-in exception logging support
- **Multiple Levels**: Info, Warning, Error, Debug levels
- **Console Output**: Logs to stdout for Azure Functions compatibility

## Development Workflow

### 1. Local Development Setup
```powershell
# Install dependencies
pip install -r requirements.txt

# Run locally
func start
```

### 2. Testing Endpoints
- Test Functions:
  - `GET/POST http://localhost:7071/api/test/hello`

### 3. Adding Dependencies
Update `requirements.txt` when adding new packages:
```
azure-functions
# Add your new dependencies here
```

## Best Practices

1. **Module Organization**: Keep related functions together in the same module
2. **Logging**: Always use the custom logger for consistent log formatting
3. **Error Handling**: Implement proper error handling and logging in all functions
4. **Documentation**: Add docstrings to all functions explaining their purpose
5. **Testing**: Test each function locally before deploying
6. **Route Naming**: Use clear, RESTful route naming conventions
7. **Function Isolation**: Keep functions focused on single responsibilities

## Current Modules

### TestFunctions
- **Purpose**: Contains test and sample functions for development
- **Functions**:
  - `hello_test_function`: Basic hello world test function
- **Routes**:
  - `GET/POST /api/test/hello`



## Git Workflow

This project follows a dual-repository strategy with specific branching conventions. **Please read the [Branching Strategy](BRANCHING_STRATEGY.md) document** for complete details.

### Quick Start
1. **Development Repository**: Azure repository (organization access required)
2. **Branch Convention**: `{YourInitials}/{UserStoryNumber}` (e.g., `NA/1234`)
3. **Workflow**: Feature branch → Code Review → Main → Release
4. **GitHub Repository**: Read-only mirror, no direct contributions

### Essential Commands
```bash
# Start new feature
git checkout main && git pull origin main
git checkout -b {YourInitials}/{StoryNumber}

# Daily development
git add . && git commit -m "feat(module): description"
git push origin {YourInitials}/{StoryNumber}

# After PR approval
git checkout main && git pull origin main
git branch -d {YourInitials}/{StoryNumber}
```

## Deployment

### Azure Deployment
1. Ensure all dependencies are in `requirements.txt`
2. Deploy using Azure Functions Core Tools or VS Code Azure Functions extension
3. Configure environment variables in Azure portal if needed

### Environment Configuration
- Local settings: `local.settings.json`
- Production settings: Configure in Azure Portal under Configuration

---

For questions or contributions, please follow the established patterns and naming conventions outlined in this README and the [Branching Strategy](BRANCHING_STRATEGY.md) document.
