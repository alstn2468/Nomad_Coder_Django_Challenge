from core.management.commands.custom_command import CustomCommand
from categories.models import Category
from random import choice


class Command(CustomCommand):
    help = "Automatically create categories"

    def handle(self, *args, **options):
        try:
            categories = [
                "Crime Thriller",
                "Disaster Thriller",
                "Psychological Thriller",
                "Techno Thriller",
                "War and Military Action",
                "Spy and Espionage Action",
                "Martial Arts Action",
                "Western Shoot ‘Em Up Action",
                "Action Hybrid Genres",
                "Slapstick Comedy",
                "Screwball Comedy",
                "Parody Comedy",
                "Black Comedy",
                "Zombie Horror",
                "Folk Horror",
                "Body Horror",
                "Found Footage Horror",
                "Space Travel",
                "Time Travel",
                "Cerebral Science",
                "Robot and Monster Films",
                "Disaster and Alien Invasion",
                "Classic Western",
                "The Revisionist and Anti-Western",
                "Contemporary and Neo-Western",
                "Fantasy and Space Western",
                "Modern Western",
                "Historical Romance",
                "Romantic Drama",
                "Romantic Comedy",
                "Chick Flick",
                "Paranormal Romance",
                "Conspiracy Thriller",
                "Crime Thriller",
                "Legal Thriller",
                "Spy Thriller",
                "Supernatural Thriller",
            ]

            self.stdout.write(self.style.SUCCESS("■ START CREATE CATEGORIES"))

            for idx, name in enumerate(categories):
                Category.objects.create(
                    name=name,
                    kind=choice(
                        [
                            Category.KIND_BOOK,
                            Category.KIND_MOVIE,
                            Category.KIND_BOTH,
                        ]
                    ),
                )
                self.progress_bar(
                    idx + 1,
                    len(categories),
                    prefix="■ PROGRESS",
                    suffix="Complete",
                    length=40,
                )

            self.stdout.write(self.style.SUCCESS("■ SUCCESS CREATE ALL CATEGORIES!"))

        except Exception as e:
            self.stdout.write(self.style.ERROR(f"■ {e}"))
            self.stdout.write(self.style.ERROR("■ FAIL CREATE CATEGORIES"))