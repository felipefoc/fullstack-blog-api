from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import RegistrationAPIView
from django.urls import include, path
from rest_framework.routers import DefaultRouter


urlpatterns = [
    #path('api/v1/auth/auth-token', obtain_auth_token, name='obtain-auth-token')
    path('auth/register/', RegistrationAPIView.as_view(), name='register'),
    path('auth/login/', TokenObtainPairView.as_view(), name='login'),
    path('auth/refresh-token', TokenRefreshView.as_view(), name='refreshtoken'),

]