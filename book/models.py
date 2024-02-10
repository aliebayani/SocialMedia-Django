from django.db import models

from django.urls import reverse


class Book(models.Model):
    BookName = models.CharField(max_length=100)
    BookInfo = models.TextField()

    def __str__(self):
        return self.BookName

    def get_absolute_url(self):
        return reverse('book-detail', kwargs={'pk': self.pk})
