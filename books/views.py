from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
)
from django.http import Http404
from django.shortcuts import redirect, reverse
from books.models import Book


class BookListView(ListView):
    model = Book
    paginate_by = 10
    paginate_orphans = 5
    ordering = "created_at"
    context_object_name = "books"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "All Books"
        return context

    def dispatch(self, request, *args, **kwargs):
        try:
            return super(BookListView, self).dispatch(request, *args, **kwargs)

        except Http404:
            return redirect(reverse("core:home"))


class BookDetailView(DetailView):
    model = Book

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        book = kwargs["object"]
        context["page_title"] = book.title

        return context


class BookCreateView(CreateView):
    model = Book
    fields = [
        "title",
        "year",
        "cover_image",
        "category",
        "writer",
        "rating",
    ]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "BOOK CREATE"

        return context


class BookUpdateView(UpdateView):
    model = Book
    fields = [
        "title",
        "year",
        "cover_image",
        "category",
        "writer",
        "rating",
    ]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "BOOK UPDATE"

        return context