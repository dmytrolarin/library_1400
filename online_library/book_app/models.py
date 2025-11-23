from django.db import models
from django.urls import reverse


class Book(models.Model):
    title = models.CharField(max_length= 255)
    description = models.TextField()
    year = models.PositiveIntegerField()
    content = models.TextField()

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('book_detail', kwargs={'book_id': self.id})