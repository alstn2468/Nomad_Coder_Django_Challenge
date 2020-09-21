from categories.models import Category

def add_categories_to_context(request):
    return {
        "categories": Category.objects.all()
    }