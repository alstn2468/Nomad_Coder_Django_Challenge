from django.urls import path
from people.views import (
    PersonListView,
    PersonDetailView,
    PersonCreateView,
    PersonUpdateView,
)

app_name = "people"

urlpatterns = [
    path("", PersonListView.as_view(), name="people"),
    path("create", PersonCreateView.as_view(), name="people_create"),
    path("update/<int:pk>", PersonUpdateView.as_view(), name="people_update"),
    path("<int:pk>", PersonDetailView.as_view(), name="people_detail"),
]
