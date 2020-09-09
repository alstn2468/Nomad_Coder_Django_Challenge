from django.shortcuts import render


def people_list(request):
    return render(request, "peoples/people_list.html")