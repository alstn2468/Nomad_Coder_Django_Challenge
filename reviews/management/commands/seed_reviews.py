from core.management.commands.custom_command import CustomCommand
from django_seed import Seed
from random import choice, uniform
from reviews.models import Review
from movies.models import Movie
from books.models import Book
from users.models import User


class Command(CustomCommand):
    help = "Automatically create reviews"

    def add_arguments(self, parser):
        parser.add_argument("--total", default=1, help="Number of reviews to create")

    def handle(self, *args, **options):
        try:
            total = int(options.get("total"))

            self.stdout.write(self.style.SUCCESS("■ START CREATE MOVIE REVIEWS"))

            users = User.objects.all()
            movies = Movie.objects.all()

            for idx, movie in enumerate(movies):
                seeder = Seed.seeder()
                seeder.add_entity(
                    Review,
                    total,
                    {
                        "rating": lambda x: uniform(0.0, 5.0),
                        "movie": movie,
                        "text": seeder.faker.sentence(),
                        "created_by": lambda x: choice(users),
                    },
                )

                self.progress_bar(
                    idx + 1,
                    len(movies),
                    prefix="■ PROGRESS",
                    suffix="Complete",
                    length=40,
                )

                seeder.execute()

            self.stdout.write(self.style.SUCCESS("■ SUCCESS CREATE MOVIE REVIEWS!"))

            self.stdout.write(self.style.SUCCESS("■ START CREATE BOOK REVIEWS"))

            books = Book.objects.all()

            for idx, book in enumerate(books):
                seeder = Seed.seeder()
                seeder.add_entity(
                    Review,
                    total,
                    {
                        "rating": lambda x: uniform(0.0, 5.0),
                        "book": book,
                        "text": seeder.faker.sentence(),
                        "created_by": lambda x: choice(users),
                    },
                )

                self.progress_bar(
                    idx + 1,
                    len(books),
                    prefix="■ PROGRESS",
                    suffix="Complete",
                    length=40,
                )

                seeder.execute()

            self.stdout.write(self.style.SUCCESS("■ SUCCESS CREATE BOOK REVIEWS!"))

        except Exception as e:
            self.stdout.write(self.style.ERROR(f"■ {e}"))
            self.stdout.write(self.style.ERROR("■ FAIL CREATE REVIEWS"))