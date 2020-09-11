from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage
from movies.models import Movie
from books.models import Book
from people.models import Person


def resolve_home(request):
    page = request.GET.get("page", 1)

    movies = Movie.objects.all().order_by("-created_at")
    books = Book.objects.all().order_by("-created_at")
    people = Person.objects.all().order_by("-created_at")

    try:
        movies_paginator = Paginator(movies, 10, orphans=5)
        movies = movies_paginator.page(int(page))
    except EmptyPage:
        movies = None

    try:
        books_paginator = Paginator(books, 10, orphans=5)
        books = books_paginator.page(int(page))
    except EmptyPage:
        books = None

    try:
        people_paginator = Paginator(people, 10, orphans=5)
        people = people_paginator.page(int(page))
    except EmptyPage:
        people = None

    return render(
        request,
        "home/home.html",
        {
            "movies": movies,
            "books": books,
            "people": people,
            "current_page": page,
        },
    )


def resolve_search(request):
    return render(request, "search/search.html")
