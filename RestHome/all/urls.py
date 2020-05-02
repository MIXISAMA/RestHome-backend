from django.urls import path
from all.views import TestEndpoint, AuthToken

urlpatterns = [
    path("test_endpoint/", TestEndpoint.as_view()),
    path("login/", AuthToken.as_view()),
]
