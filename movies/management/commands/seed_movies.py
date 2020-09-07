from core.management.commands.custom_command import CustomCommand
from django.contrib.admin.utils import flatten
from django_seed import Seed
from random import choice, randint, uniform
from movies.models import Movie
from categories.models import Category
from people.models import Person


class Command(CustomCommand):
    help = "Automatically create movies"

    def add_arguments(self, parser):
        parser.add_argument("--total", default=1, help="Number of movies to create")

    def handle(self, *args, **options):
        try:
            total = int(options.get("total"))

            self.stdout.write(self.style.SUCCESS("■ START CREATE MOVIES"))

            persons = Person.objects.all()
            categories = Category.objects.all()

            seeder = Seed.seeder()
            seeder.add_entity(
                Movie,
                total,
                {
                    "title": lambda x: seeder.faker.word(),
                    "year": lambda x: randint(1960, 2020),
                    "rating": lambda x: round(uniform(0.0, 5.0), 1),
                    "category": lambda x: choice(categories),
                    "director": lambda x: choice(persons),
                },
            )

            clean_pk_list = flatten(list(seeder.execute().values()))

            for idx, pk in enumerate(clean_pk_list):
                movie = Movie.objects.get(pk=pk)
                BOOLEAN = [True, False]
                self.progress_bar(
                    idx + 1, total, prefix="■ PROGRESS", suffix="Complete", length=40
                )

                for person in persons:
                    if choice(BOOLEAN):
                        movie.cast.add(person)

            self.stdout.write(self.style.SUCCESS("■ SUCCESS CREATE ALL MOVIES!"))

        except Exception as e:
            self.stdout.write(self.style.ERROR(f"■ {e}"))
            self.stdout.write(self.style.ERROR("■ FAIL CREATE MOVIES"))