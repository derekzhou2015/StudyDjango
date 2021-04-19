from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index),
    path('books/add', views.books_add),
    re_path(r'^books/edit/(?P<id>\d+)', views.books_edit),
    path('books/del', views.books_delete),

    path('authors/', views.authors),
    path('authors/add', views.authors_add),
    re_path(r'^authors/edit/(?P<id>\d+)', views.authors_edit),
    path('authors/del', views.authors_delete),

    path('publishers/', views.publishers),
    path('publishers/add', views.publishers_add),
    path('publishers/del', views.publishers_delete),
    re_path(r'^publishers/edit/(?P<id>\d+)', views.publishers_edit)
]
