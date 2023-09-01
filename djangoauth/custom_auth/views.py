from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse
from rest_framework_simplejwt.authentication import JWTAuthentication

JWT_authenticator = JWTAuthentication()


def get_name(request):
    response = JWT_authenticator.authenticate(request)
    if response is not None:
        # unpacking
        user, token = response
        print("this is decoded token claims", token.payload)
    else:
        print("no token is provided in the header or the header is missing")
    return HttpResponse("Hello world!")
