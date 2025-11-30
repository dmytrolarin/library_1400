from django.urls import path
from .views import *

urlpatterns = [
    path('', render_authors, name='authors'),
    path('author_detail/<int:author_id>', render_author_detail, name='author_detail')
]