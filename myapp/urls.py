from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name="index"),
    path("shortly",views.shortly,name="shortly"),
    path("<str:pk>",views.go,name="go"),
]