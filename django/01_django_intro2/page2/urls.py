from page2 import views
from django.urls import path

urlpatterns = [
    path('static_sample/' , views.static_sample),
    path('user_create/' , views.user_create),
    path('user_new/' , views.user_new),
    path('asciiart/' , views.asciiart),
    path('result/' , views.result),
    path('catch/' , views.catch),
    path('throw/' , views.throw),
    path('' , views.index),
    path('index/' , views.index),
    path('gong/', views.gong),
]


