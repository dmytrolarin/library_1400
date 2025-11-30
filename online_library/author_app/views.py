from django.shortcuts import render
from .models import Author
from django.shortcuts import get_object_or_404

def render_authors(request):
    authors = Author.objects.all()
    return render(request, "author_app/authors.html", context= {'authors': authors})

def render_author_detail(request, author_id):
    author = get_object_or_404(Author, id = author_id)
    return render(request, 'author_app/author_detail.html', context = {"author": author})