from django.urls import path
from main import views
from main.models import Query

urlpatterns = [
    path("", views.home, name="home"),
]