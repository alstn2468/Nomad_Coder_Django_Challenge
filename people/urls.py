from django.urls import path
from people.views import PersonListView

app_name = "people"

urlpatterns = [
    path("", PersonListView.as_view(), name="people"),
]
