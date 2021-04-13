from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import CreateUserAPIView
from django.urls import include, path
from rest_framework.routers import DefaultRouter



urlpatterns = [
    #path('api/v1/auth/auth-token', obtain_auth_token, name='obtain-auth-token')
    path('register/', CreateUserAPIView.as_view()),
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('refresh-token/', TokenRefreshView.as_view(), name='refreshtoken'),

]

