from django.urls import path
from .views import (
    AuthorListView,
    AuthorDetailView,
)
from . import views

urlpatterns = [
    path('', AuthorListView.as_view(), name='author-list'),
    path('author/<int:pk>/', AuthorDetailView.as_view(), name='author-detail'),

]
