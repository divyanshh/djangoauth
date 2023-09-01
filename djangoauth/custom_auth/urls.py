from django.urls import path, include

from . import views
from rest_framework.routers import DefaultRouter
from .views import UserViewSet

# Create a router for the UserViewSet
router = DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('api/user/profile/', views.UserProfileView.as_view(), name='user-profile'),
    path('apii/', include(router.urls)),
]
