from django.urls import path
from people.views import PersonListView, PersonDetailView

app_name = "people"

urlpatterns = [
    path("", PersonListView.as_view(), name="people"),
    path("<int:pk>", PersonDetailView.as_view(), name="people_detail"),
]
