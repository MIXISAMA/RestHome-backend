from django.urls import path
from old.views import Olds, Register

urlpatterns = [
    path("register/", Register.as_view()),
    path("olds/", Olds.as_view()),
    path("olds/<str:username>/", Olds.as_view()),
]
