from django.urls import path
from all.views import TestEndpoint

urlpatterns = [
    path("test_endpoint/", TestEndpoint.as_view()),
]
