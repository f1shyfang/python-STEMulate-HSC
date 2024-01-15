from django.urls import path
from . import views



#url conf
urlpatterns = [

    path('playground/hello', views.say_hello)
]