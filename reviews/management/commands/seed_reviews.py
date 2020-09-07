from core.management.commands.custom_command import CustomCommand
from django_seed import Seed
from random import choice, randint
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

            self.stdout.write(self.style.SUCCESS("■ START CREATE REVIEWS"))

            users = User.objects.all()
            movies = Movie.objects.all()
            books = Book.objects.all()

            for idx, (movie, book) in enumerate(zip(movies, books)):
                seeder = Seed.seeder()
                seeder.add_entity(
                    Review,
                    total,
                    {
                        "rating": lambda x: randint(0, 6),
                        "movie": movie,
                        "book": book,
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

            self.stdout.write(self.style.SUCCESS("■ SUCCESS CREATE REVIEWS!"))

        except Exception as e:
            self.stdout.write(self.style.ERROR(f"■ {e}"))
            self.stdout.write(self.style.ERROR("■ FAIL CREATE REVIEWS"))