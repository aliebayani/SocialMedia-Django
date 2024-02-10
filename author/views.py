from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
 
)
from .models import Author

class AuthorListView(ListView):
    model = Author
    template_name = 'author/Author_list.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'authors'
 

class AuthorDetailView(DetailView):
    model = Author

