from django.urls import path

from . import views

urlpatterns = [
    #con name me puedo apuntar a la ruta desde template usando {% url 'appname/login' %} por ejemplo
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout")
]