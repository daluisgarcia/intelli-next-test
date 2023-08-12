import csv

from django.core.management.base import BaseCommand
from api.models import Book


class Command(BaseCommand):
    help = "Seeds the database with CSV files inside csv/ folder in root"

    def handle(self, *args, **options):

        print("Seeding books...")

        books_added = 0
        with open('csv/books.csv', 'r', encoding='latin-1') as f:
            reader = csv.reader(f, delimiter=';', quotechar='"', skipinitialspace=True, escapechar='&')

            is_header = True
            for row in reader:
                if is_header:
                    is_header = False
                    continue

                try:
                    _, created = Book.objects.get_or_create(
                        isbn=row[0],
                        title=row[1],
                        author=row[2],
                        year_of_publication=int(row[3]),
                        publisher=row[4],
                        image_url_s=row[5],
                        image_url_m=row[6],
                        image_url_l=row[7],
                    )
                except ValueError:
                    print(f'The value of line with isbn {row[0]} could not be inserted')
                    continue

                if not created:
                    print(f"Book with isbn {row[0]} already exists")
                    continue

                books_added += 1

        print(f"Books seeded successfully: {books_added}")
