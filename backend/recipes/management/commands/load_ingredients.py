import json
import os

from django.conf import settings
from django.core.management.base import BaseCommand

from recipes.models import Ingredient


class Command(BaseCommand):
    help = 'Load ingredients from JSON file'

    def handle(self, *args, **kwargs):
        data_path = os.path.join(
            settings.BASE_DIR.parent, 'data', 'ingredients.json'
        )
        if not os.path.exists(data_path):
            data_path = '/app/data/ingredients.json'
        with open(data_path, encoding='utf-8') as f:
            data = json.load(f)
        try:
            Ingredient.objects.bulk_create(
                (Ingredient(**item) for item in data),
                ignore_conflicts=True
            )
            self.stdout.write(
                self.style.SUCCESS(
                    'Loaded ' + str(Ingredient.objects.count()) + ' ingredients.'
                )
            )
        except Exception as e:
            self.stdout.write(
                self.style.ERROR('Error loading ingredients: ' + str(e))
            )
