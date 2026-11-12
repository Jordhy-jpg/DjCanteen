from django.core.management.base import BaseCommand

from catalogue.models import Product


class Command(BaseCommand):
    help = "Set stock to 20 for all existing products without changing other fields."

    def handle(self, *args, **options):
        updated = Product.objects.update(stock=20)
        self.stdout.write(self.style.SUCCESS(
            f"Seeded stock to 20 for {updated} products."
        ))
