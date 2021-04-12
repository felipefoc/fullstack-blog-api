from django.urls import include, path
from rest_framework.routers import DefaultRouter



routers = DefaultRouter()
# routers.register('name_of_class', Class_Name, basename='somename')


urlpatterns = [path("", include(routers.urls))]