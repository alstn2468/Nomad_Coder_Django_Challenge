from django.shortcuts import render


def home(request):
    return render(request, "home/home.html")


def search(request):
    return render(request, "search/search.html")


def genre(request):
    return render(request, "genres/genre_list.html")