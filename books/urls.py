from django.urls import path
from books.views import BookListView, BookDetailView, BookCreateView, BookUpdateView

app_name = "books"

urlpatterns = [
    path("", BookListView.as_view(), name="books"),
    path("create", BookCreateView.as_view(), name="book_create"),
    path("update/<int:pk>", BookUpdateView.as_view(), name="book_update"),
    path("<int:pk>", BookDetailView.as_view(), name="book_detail"),
]
