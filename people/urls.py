from django.urls import path
from people.views import people_list

app_name = "people"

urlpatterns = [
    path("", people_list, name="people_list"),
]