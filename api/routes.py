from django.urls import path, include
from .fbvviews import function_based_view
from .genericviews import ListAndCreate, RetrieveUpdateDestroy


urlpatterns = [
    path('fbv/', function_based_view, name="fbv"),
    path('fbv/<int:pk>', function_based_view, name="fbv2"),
    path('genericviews/', ListAndCreate.as_view()),
    path('genericviews/<str:username>', RetrieveUpdateDestroy.as_view()),
]