from django.shortcuts import render


def resolve_categories(request):
    return render(
        request,
        "genre.html",
        {
            "page_title": "Genre",
        },
    )
