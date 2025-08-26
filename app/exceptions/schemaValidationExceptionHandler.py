from fastapi import Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError

async def validationExceptionHandler(request: Request, exception: RequestValidationError):
    errors = exception.errors()
    for error in errors:
        if error.get("type") == "url_parsing":
            return JSONResponse(
                status_code=422,
                content={"detail": "Invalid URL. Please provide a valid URL."}
            )
    return JSONResponse(status_code=422, content={"detail": errors})
