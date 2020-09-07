from core.management.commands.custom_command import CustomCommand
from django_seed import Seed
from random import choice, randint, uniform
from books.models import Book
from categories.models import Category
from people.models import Person


class Command(CustomCommand):
    help = "Automatically create books"

    def add_arguments(self, parser):
        parser.add_argument("--total", default=1, help="Number of books to create")

    def handle(self, *args, **options):
        try:
            total = int(options.get("total"))

            self.stdout.write(self.style.SUCCESS("■ START CREATE BOOKS"))

            persons = Person.objects.all()
            categories = Category.objects.all()

            seeder = Seed.seeder()
            seeder.add_entity(
                Book,
                total,
                {
                    "title": lambda x: seeder.faker.word(),
                    "year": lambda x: randint(1960, 2020),
                    "rating": lambda x: round(uniform(0.0, 5.0), 1),
                    "category": lambda x: choice(categories),
                    "writer": lambda x: choice(persons),
                },
            )
            seeder.execute()

            self.stdout.write(self.style.SUCCESS("■ SUCCESS CREATE ALL BOOKS!"))

        except Exception as e:
            self.stdout.write(self.style.ERROR(f"■ {e}"))
            self.stdout.write(self.style.ERROR("■ FAIL CREATE BOOKS"))