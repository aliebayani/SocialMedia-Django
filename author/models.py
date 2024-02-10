from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from book.models import Book

class Author(models.Model):
    Fullname = models.CharField(max_length=100)
    AuthorInfo = models.TextField()
    Nationality = models.CharField(max_length=25)
    Book = models.ForeignKey(Book, on_delete=models.CASCADE)
    def __str__(self):
        return self.Fullname

    def get_absolute_url(self):
        return reverse('author-detail', kwargs={'pk': self.pk})
