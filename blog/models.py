from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from author.models import Author
from book.models import Book

class Post(models.Model):
   
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    FromAuthor = models.ForeignKey(Author, on_delete=models.CASCADE)
    FromBook   = models.ForeignKey(Book,on_delete=models.CASCADE)
    Likes      = models.ManyToManyField(User,blank=True,related_name='Likes')
    Dislikes   = models.ManyToManyField(User,blank=True,related_name='Dislikes')
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
class comment(models.Model):
    comment=models.TextField()
    created_on = models.DateTimeField(default=timezone.now)
    Owner      = models.ForeignKey(User,on_delete=models.CASCADE)
    post       = models.ForeignKey(Post,on_delete=models.CASCADE)