from fastapi import HTTPException
from .types.http_bad_request_error import HttpBadRequestError

def error_handler(exception: Exception) -> HTTPException:
    if isinstance(exception, HttpBadRequestError):
        return HTTPException(
            status_code=exception.message_code,
            detail=str(exception)
        )

    return HTTPException(
        status_code=500,
        detail="Internal Server Error"
    )