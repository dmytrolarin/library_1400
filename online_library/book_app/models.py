from django.db import models
from django.urls import reverse
from author_app.models import Author

class Book(models.Model):
    title = models.CharField(max_length= 255)
    description = models.TextField()
    year = models.PositiveIntegerField()
    content = models.TextField()
    author = models.ForeignKey(Author, on_delete = models.CASCADE, null = True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('book_detail', kwargs={'book_id': self.id})