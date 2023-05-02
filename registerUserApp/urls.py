from django.urls import path
from registerUserApp.views import *

urlpatterns = [
    path("ping/", ping, name="ping"),
    path("api/usuarios/", UsuariosList.as_view()),
]