from django.urls import path
from . import views

app_name="articles"
urlpatterns = [
    path('<int:article_pk>/comments/<int:comment_pk>/delete', views.comments_delete, name='comments_delete'), # POST (comments_delete)
    path('<int:article_pk>/comments/', views.comments_create, name='comments_create'), # POST (comments_create)
    path('index/', views.index, name="index"),
    path('', views.index, name="index"),
    path('create/', views.create, name="create"),
    path('<int:article_pk>/',views.detail, name="detail"),
    path('<int:article_pk>/delete',views.delete, name="delete"),
    path('<int:article_pk>/update',views.update, name="update"),

]