from django.shortcuts import render


def resolve_categories(request):
    return render(request, "genres/genre_list.html")
