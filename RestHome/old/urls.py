from django.urls import path
from old.views import Olds

urlpatterns = [
    path("olds/", Olds.as_view()),
    path("olds/<str:username>/", Olds.as_view()),
]
