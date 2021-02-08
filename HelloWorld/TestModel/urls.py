from django.urls import path
from . import views


urlpatterns = [
    path("list/", views.list),
    path('add/', views.add),
    path('edit/', views.edit),
    path('del/', views.delete),
]
