from django.urls import path, include
from .views import function_based_view


urlpatterns = [
    path('fbv/', function_based_view, name="fbv"),
    path('fbv/<int:id>', function_based_view, name="fbv"),
    # path('fbv/<int:id>/', function_based_view_id, name="fbv_id"),
]