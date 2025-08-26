from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
# Routers
from app.router import userRouter
from app.router import urlInsightsRouter

# Exceptions
from app.exceptions import schemaValidationExceptionHandler

app = FastAPI()

# Exception Handling
app.add_exception_handler(RequestValidationError, schemaValidationExceptionHandler.validationExceptionHandler)

# Routing
app.include_router(userRouter.router)
app.include_router(urlInsightsRouter.router)
