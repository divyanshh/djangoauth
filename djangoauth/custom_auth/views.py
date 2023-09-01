from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import viewsets
from django.contrib.auth.models import User
from .serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    Enables router urls
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
class UserProfileView(APIView):
    """
    Returns user details

    fetches first name and last name from the JWT user details and returns them
    """
    def get(self, request):
        user = request.user
        response_data = {
            'first_name': user.first_name,
            'last_name': user.last_name,
        }
        return Response(response_data)
