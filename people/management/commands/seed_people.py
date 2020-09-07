from django.core.management.base import BaseCommand
from django_seed import Seed
from random import choice
from people.models import Person


class Command(BaseCommand):
    help = "Automatically create people"

    def add_arguments(self, parser):
        parser.add_argument("--total", default=1, help="Number of people to create")

    def handle(self, *args, **options):
        try:
            total = int(options.get("total"))

            self.stdout.write(self.style.SUCCESS("■ START CREATE PEOPLE"))

            seeder = Seed.seeder()
            seeder.add_entity(
                Person,
                total,
                {
                    "name": lambda x: seeder.faker.name(),
                    "kind": lambda x: choice(
                        [
                            Person.KIND_ACTOR,
                            Person.KIND_DIRECTOR,
                            Person.KIND_WRITER,
                        ]
                    ),
                },
            )
            seeder.execute()

            self.stdout.write(self.style.SUCCESS("■ SUCCESS CREATE ALL PEOPLE!"))

        except Exception as e:
            self.stdout.write(self.style.ERROR(f"■ {e}"))
            self.stdout.write(self.style.ERROR("■ FAIL CREATE PEOPLE"))