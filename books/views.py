from django.core.paginator import Paginator
from django.shortcuts import render
from books.models import Book


def resolve_books(request):
    books = Book.objects.all().order_by("-created_at")
    paginator = Paginator(books, 3)

    page_number = request.GET.get("page", 1)
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        "books/book_list.html",
        {
            "books": page_obj,
        },
    )
