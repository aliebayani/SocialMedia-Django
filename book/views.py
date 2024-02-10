from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
)
from .models import Book

class BookListView(ListView):
    model = Book
    template_name = 'book/Book_List.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'books'
 

class BookDetailView(DetailView):
    model = Book

