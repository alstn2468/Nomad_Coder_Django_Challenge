from django.urls import path
from books.views import resolve_books

app_name = "books"

urlpatterns = [path("", resolve_books, name="books")]
