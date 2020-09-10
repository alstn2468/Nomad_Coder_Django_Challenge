from django.shortcuts import render


def resolve_home(request):
    return render(request, "home/home.html")


def resolve_search(request):
    return render(request, "search/search.html")
