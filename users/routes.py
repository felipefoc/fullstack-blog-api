from rest_framework.routers import DefaultRouter
from .views import UserViewSet, AdminViewSet
from django.urls import include, path

router = DefaultRouter()
router.register(r'', UserViewSet)




urlpatterns = router.urls
