from django.shortcuts import render


def resolve_books(request):
    return render(request, "books/books.html")
