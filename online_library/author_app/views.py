from django.shortcuts import render


def render_author(request):
    return render(request, "author_app/authors.html")