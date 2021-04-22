from django.urls import path, include
from .fbvviews import function_based_view


urlpatterns = [
    path('fbv/', function_based_view, name="fbv"),
    path('fbv/<int:pk>', function_based_view, name="fbv2"),
    # path('fbv/<int:id>/', function_based_view_id, name="fbv_id"),
]