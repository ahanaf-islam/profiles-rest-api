from django.urls import path

from profiles_api import views
from . import views


urlpatterns = [
    path('hello-view/',views.HelloApiView.as_view()),
]