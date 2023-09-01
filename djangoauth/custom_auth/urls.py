from django.urls import path, include

from custom_auth import views

urlpatterns = [
    path('/user/profile/', views.get_name, name='get_name'),
]
