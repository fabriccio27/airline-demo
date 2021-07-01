from django.urls import path
from . import views

app_name = "flights"
#no tener esto definido hacia que cuando queria ir al index de la app de flights, me mandaba al index de la app de users

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:flight_id>", views.flight, name="flight"),
    path("<int:flight_id>/book", views.book, name="book"),
]
