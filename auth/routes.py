from .views import RegisterView
from django.urls import include, path
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('register', RegisterView, basename="register")

urlpatterns = [
    #path('api/v1/auth/auth-token', obtain_auth_token, name='obtain-auth-token')
    path('',include(router.urls)),
]

