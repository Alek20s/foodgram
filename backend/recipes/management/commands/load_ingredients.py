import json
import os

from django.core.management.base import BaseCommand

from recipes.models import Ingredient


class Command(BaseCommand):
    help = 'Load ingredients from JSON file'

    def handle(self, *args, **kwargs):
        data_path = os.path.join(
            os.path.dirname(__file__),
            '..', '..', '..', '..', 'data', 'ingredients.json'
        )
        with open(data_path, encoding='utf-8') as f:
            data = json.load(f)
        Ingredient.objects.bulk_create([
            Ingredient(
                name=item['name'],
                measurement_unit=item['measurement_unit']
            )
            for item in data
        ], ignore_conflicts=True)
        self.stdout.write(
            self.style.SUCCESS(
                f'Loaded {Ingredient.objects.count()} ingredients.'
            )
        )
