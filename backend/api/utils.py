from django.db.models import Sum

from recipes.models import RecipeIngredient


def get_shopping_cart_content(user):
    ingredients = RecipeIngredient.objects.filter(
        recipe__shopping_cart__user=user
    ).values(
        'ingredient__name', 'ingredient__measurement_unit'
    ).annotate(total=Sum('amount'))

    lines = [
        f"{item['ingredient__name']} "
        f"({item['ingredient__measurement_unit']}) — {item['total']}"
        for item in ingredients
    ]
    return '\n'.join(lines)
