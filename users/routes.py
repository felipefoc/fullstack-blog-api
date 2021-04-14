from rest_framework.routers import DefaultRouter
from .views import UserViewSet, AdminViewSet
from django.urls import include, path

router = DefaultRouter()
router.register(r'', UserViewSet)
router.register(r'admins', AdminViewSet)



urlpatterns = router.urls
