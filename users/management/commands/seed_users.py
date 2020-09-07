from django.core.management.base import BaseCommand
from django_seed import Seed
from random import choice
from users.models import User
from categories.models import Category


class Command(BaseCommand):
    help = "Automatically create users"

    def add_arguments(self, parser):
        parser.add_argument("--total", default=1, help="Number of users to create")

    def handle(self, *args, **options):
        try:
            total = int(options.get("total"))

            self.stdout.write(self.style.SUCCESS("■ START CREATE USERS"))

            categories = Category.objects.all()

            seeder = Seed.seeder()
            seeder.add_entity(
                User,
                total,
                {
                    "is_staff": False,
                    "is_superuser": False,
                    "bio": lambda x: seeder.faker.sentence(),
                    "preference": lambda x: choice(
                        [
                            User.PREF_BOOKS,
                            User.PREF_MOVIES,
                        ]
                    ),
                    "language": lambda x: choice(
                        [
                            User.LANG_EN,
                            User.LANG_KR,
                        ]
                    ),
                    "fav_book_cat": lambda x: choice(categories),
                    "fav_movie_cat": lambda x: choice(categories),
                },
            )
            seeder.execute()

            self.stdout.write(self.style.SUCCESS("■ SUCCESS CREATE ALL USERS!"))

        except Exception as e:
            self.stdout.write(self.style.ERROR(f"■ {e}"))
            self.stdout.write(self.style.ERROR("■ FAIL CREATE USERS"))