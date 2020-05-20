from django.urls import path
from employee.views import Rooms, OrderForms, Emps

urlpatterns = [
    path("rooms/", Rooms.as_view()),
    path("rooms/<str:id>/", Rooms.as_view()),
    path("order_forms/", OrderForms.as_view()),
    path("order_forms/<str:id>/", OrderForms.as_view()),
    path("emps/", Emps.as_view()),
    path("emps/<str:username>/", Emps.as_view()),
    path("employees/", Emps.as_view()),
    path("employees/<str:username>/", Emps.as_view()),
]