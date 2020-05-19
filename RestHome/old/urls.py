from django.urls import path
from old.views import Olds, Login

urlpatterns = [
    path("login/", Login.as_view()),
    path("olds/", Olds.as_view()),
    path("olds/<str:username>/", Olds.as_view()),
]
