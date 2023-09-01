# your_app/middleware/jwt_middleware.py

from rest_framework_simplejwt.authentication import JWTAuthentication


class JWTMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        """
        :param request:
        :return: response with updated user details

        If the token is valid, we update the request with user details
        If the token is invalid, we let the flow continue as usual
        """
        auth_header = request.META.get('HTTP_AUTHORIZATION', '')
        if auth_header.startswith('Bearer '):
            jwt_auth = JWTAuthentication()
            user, _ = jwt_auth.authenticate(request)
            if user is not None:
                request.custom_user = user
        response = self.get_response(request)
        return response
