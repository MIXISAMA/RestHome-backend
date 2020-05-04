from django.urls import path
from all.views import TestEndpoint, AuthToken, Companies, Announcements

urlpatterns = [
    path("test_endpoint/", TestEndpoint.as_view()),
    path("login/", AuthToken.as_view()),
    path("companies/", Companies.as_view()),
    path("announcements/", Announcements.as_view()),
]
