from django.core.paginator import Paginator
from django.shortcuts import render
from people.models import Person


def resolve_people(request):
    persons = Person.objects.all().order_by("-created_at")
    paginator = Paginator(persons, 3)

    page_number = request.GET.get("page", 1)
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        "people/people_list.html",
        {
            "persons": page_obj,
        },
    )
