from django.shortcuts import render
from .models import Book
from django.shortcuts import get_object_or_404

def render_books(request):
    list_books = Book.objects.all()
    return render(request, 'book_app/books.html', context = {"list_books" : list_books})

def render_book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    return render(request, 'book_app/book_detail.html', context={"book": book})