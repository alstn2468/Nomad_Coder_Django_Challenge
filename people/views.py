from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
)
from django.http import Http404
from django.shortcuts import redirect, reverse
from people.models import Person


class PersonListView(ListView):
    model = Person
    paginate_by = 10
    paginate_orphans = 5
    ordering = "created_at"
    context_object_name = "people"
    template_name = "people/people_list.html"

    def dispatch(self, request, *args, **kwargs):
        try:
            return super(PersonListView, self).dispatch(request, *args, **kwargs)

        except Http404:
            return redirect(reverse("core:home"))


class PersonDetailView(DetailView):
    model = Person
    template_name = "people/person_detail.html"
    context_object_name = "person"


class PersonCreateView(CreateView):
    model = Person
    fields = [
        "name",
        "photo",
        "kind",
    ]


class PersonUpdateView(UpdateView):
    model = Person
    fields = [
        "name",
        "photo",
        "kind",
    ]
