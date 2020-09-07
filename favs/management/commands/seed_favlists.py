from django.contrib.admin.utils import flatten
from core.management.commands.custom_command import CustomCommand
from django_seed import Seed
from random import randint, choice
from movies.models import Movie
from books.models import Book
from users.models import User
from favs.models import FavList


class Command(CustomCommand):
    help = "Automatically create fav lists"

    def add_arguments(self, parser):
        parser.add_argument("--total", default=1, help="Number of fav lists to create")

    def handle(self, *args, **options):
        try:
            total = int(options.get("total"))

            self.stdout.write(self.style.SUCCESS("■ START CREATE FAV LISTS"))

            users = User.objects.all()
            books = Book.objects.all()
            movies = Movie.objects.all()

            seeder = Seed.seeder()
            seeder.add_entity(
                FavList,
                total,
                {"created_by": lambda x: choice(users)},
            )

            clean_pk_list = flatten(list(seeder.execute().values()))

            for idx, pk in enumerate(clean_pk_list):
                self.progress_bar(
                    idx + 1,
                    len(clean_pk_list),
                    prefix="■ PROGRESS",
                    suffix="Complete",
                    length=40,
                )

                fav_list_model = FavList.objects.get(pk=pk)
                books = books[randint(0, 5) : randint(6, len(books))]
                movies = movies[randint(0, 5) : randint(6, len(movies))]

                fav_list_model.books.add(*books)
                fav_list_model.movies.add(*movies)

            self.stdout.write(self.style.SUCCESS("■ SUCCESS CREATE ALL FAV LISTS!"))

        except Exception as e:
            self.stdout.write(self.style.ERROR(f"■ {e}"))
            self.stdout.write(self.style.ERROR("■ FAIL CREATE FAV LISTS"))