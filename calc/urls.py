from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("check_availability",views.check_availability, name="check_availability"),
    path("home", views.home, name="home"),
    path("reset", views.reset, name="home"),
    path("exit", views.exit, name="exit"),  
    path("entry", views.entry )
]

