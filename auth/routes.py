from .views import CreateUserAPIView
from django.urls import include, path
from rest_framework.routers import DefaultRouter



urlpatterns = [
    #path('api/v1/auth/auth-token', obtain_auth_token, name='obtain-auth-token')
    path('register/', CreateUserAPIView.as_view()),
]

