from django.urls import path
from books.views import BookListView, BookDetailView

app_name = "books"

urlpatterns = [
    path("", BookListView.as_view(), name="books"),
    path("/<int:pk>", BookDetailView.as_view(), name="book_detail"),
]
