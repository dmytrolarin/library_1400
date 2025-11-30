from django.db import models
from django.urls import reverse

class Author(models.Model):
    name = models.CharField(max_length = 255)
    surname = models.CharField(max_length = 255)
    biography = models.TextField()

    def __str__(self):
        author = f"{self.name} {self.surname}"
        return author
    
    def get_absolute_url(self):
        return reverse('author_detail', kwargs={'author_id': self.id})