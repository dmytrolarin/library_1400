from django.urls import path
from .views import render_books, render_book_detail


urlpatterns = [
    path(route='', view=render_books, name='books'),
    path(route='book-detail/<int:book_id>', view=render_book_detail, name='book_detail')
]