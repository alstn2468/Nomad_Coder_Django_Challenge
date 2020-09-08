from django.contrib.admin.utils import flatten
from django.db import IntegrityError
from copy import deepcopy
from django_seed import Seed
from random import randint, choice
from movies.models import Movie
from books.models import Book
from users.models import User
from favs.models import FavList
from core.management.commands.custom_command import CustomCommand


class Command(CustomCommand):
    help = "Automatically create fav lists"

    def handle(self, *args, **options):
        try:
            self.stdout.write(self.style.SUCCESS("■ START CREATE FAV LISTS"))

            users = User.objects.all()
            books = Book.objects.all()
            movies = Movie.objects.all()

            for idx, user in enumerate(users):
                self.progress_bar(
                    idx + 1,
                    len(users),
                    prefix="■ PROGRESS",
                    suffix="Complete",
                    length=40,
                )

                try:
                    fav_list = FavList.objects.create(created_by=user)

                    selected_books = books[randint(0, 5) : randint(6, len(books))]
                    selected_movies = movies[randint(0, 5) : randint(6, len(movies))]

                    fav_list.books.add(*selected_books)
                    fav_list.movies.add(*selected_movies)

                    fav_list.save()
                except IntegrityError:
                    continue

            self.stdout.write(self.style.SUCCESS("■ SUCCESS CREATE ALL FAV LISTS!"))

        except Exception as e:
            self.stdout.write(self.style.ERROR(f"■ {e}"))
            self.stdout.write(self.style.ERROR("■ FAIL CREATE FAV LISTS"))