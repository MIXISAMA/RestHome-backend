from django.urls import path
from employee.views import Rooms, OrderForms

urlpatterns = [
    path("rooms/", Rooms.as_view()),
    path("rooms/<str:id>/", Rooms.as_view()),
    path("order_forms/", OrderForms.as_view()),
    path("order_forms/<str:id>/", OrderForms.as_view()),
]