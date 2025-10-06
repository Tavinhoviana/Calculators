from typing import Dict
from .http_unprocessable_entity import HttpUnprocessableEntityError
from .http_bad_request import HttpUBadRequestError

def handle_errors(error: Exception) -> Dict:
    if isinstance(error, (HttpUnprocessableEntityError, HttpUBadRequestError)):
        return {
            "status_code": error.status_code, 
            "body": {
                "errors": [{
                    "title": error.name,
                    "detail": error.message
                }]
            }
        }
    
    return {
        "status_code": 500,
        "body": {
            "errors": [{
                "title": "Server error",
                "detail": str(error)
            }]
        }
    }