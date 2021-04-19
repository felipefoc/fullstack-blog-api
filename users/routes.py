from .views import test
from django.urls import include, path





urlpatterns = [
    path('', test, name='teste') 
]


