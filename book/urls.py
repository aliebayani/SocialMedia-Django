from django.urls import path
from .views import (
    BookListView,
    BookDetailView,
)
from . import views

urlpatterns = [
    path('', BookListView.as_view(), name='book-list'),
    path('book/<int:pk>/', BookDetailView.as_view(), name='book-detail'),

]
