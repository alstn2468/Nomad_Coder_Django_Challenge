from django.contrib import admin
from people.models import Person


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "kind",
        "created_at",
        "updated_at",
    )

    list_filter = ("kind",)

