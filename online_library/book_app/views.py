from django.shortcuts import render
from .models import Book


def render_books(request):
    list_books = Book.objects.all()
    return render(request, 'book_app/books.html', context = {"list_books" : list_books})