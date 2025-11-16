from django.urls import path
from .views import render_books

urlpatterns = [
    path(route='', view=render_books, name='books')
]