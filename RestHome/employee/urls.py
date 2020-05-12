from django.urls import path
from employee.views import Rooms

urlpatterns = [
    path("rooms/", Rooms.as_view()),
    path("rooms/<str:id>/", Rooms.as_view()),
]