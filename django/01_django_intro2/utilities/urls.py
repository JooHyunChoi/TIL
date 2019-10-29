from django.urls import path
from utilities import views

urlpatterns = [
    path('' , views.index),
    path('index/' , views.index),
]

