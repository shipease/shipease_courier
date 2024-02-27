# middleware to authenticate user

import jwt
from master_app.stub_models import User
from django.http import JsonResponse
import os
from django.urls import reverse

class UserJWTAuthenticationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Check if the Authorization header is present in the request
        # Check if the request path starts with the admin URL prefix
        admin_url_prefix = reverse('admin:index')  # Get the URL for the admin index view
        white_list_urls = ['/courier-api/api/schema/', '/courier-api/api/schema/swagger-ui/', '/courier-api/api/schema/redoc/']
        if request.path.startswith(admin_url_prefix) or request.path in white_list_urls:
            # This is a request to Django admin, so skip the authentication logic
            return self.get_response(request)


        authorization_header = request.headers.get('Authorization')
        if not authorization_header or not authorization_header.startswith('Bearer '):
            # If the header is missing or doesn't start with 'Bearer ', return unauthorized
            return JsonResponse({'Detail': 'Unauthorized'}, status=401)

        # Extract the token from the header
        token = authorization_header.split(' ')[1]

        try:
            # Decode the token to get the user's information
            payload = jwt.decode(token, os.getenv(
                'JWT_AUTH_SECRET_KEY'), algorithms=['HS256'])
            # payload['user_id']
            # Use a non-default database connection to retrieve the user
            try:
                user_data = User.objects.values('id', 'seller', 'user_department').using(
                    "user_db").get(id=payload['user_id'])
            except User.DoesNotExist:
                return JsonResponse({"error": "User doesn't exist"}, status=400)
            
            #add user info to current request
            request.user_data = user_data

        except jwt.ExpiredSignatureError:
            # Handle expired token
            return JsonResponse({'error': 'Token has expired'}, status=401)
        except jwt.InvalidTokenError:
            # Handle invalid token
            return JsonResponse({'error': 'Invalid token'}, status=401)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=401)

        # Continue with the request
        response = self.get_response(request)
        return response
