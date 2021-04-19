from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('add/', views.add),
    path('edit/', views.edit),
    path('del/', views.delete),
]
