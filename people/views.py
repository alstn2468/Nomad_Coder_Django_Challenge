from django.shortcuts import render


def resolve_people(request):
    return render(request, "people/people_list.html")
