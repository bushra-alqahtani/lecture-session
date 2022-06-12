from django.urls import path
from . import views

urlpatterns=[

path("",views.index),
path("add_to_card",views.add_to_card),


]