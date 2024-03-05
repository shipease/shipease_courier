from rest_framework.exceptions import ValidationError
from rest_framework.exceptions import APIException
from rest_framework.views import exception_handler

def custom_exception_handler(exc, context):
    # Call Django's default exception handler first
    response = exception_handler(exc, context)

    if response is not None:
        # Check if the exception is a ValidationError
        if isinstance(exc, ValidationError):
            # Customize the status code to 400
            response.status_code = 400
        elif isinstance(exc, APIException):
            response.status_code = 400

    return response
