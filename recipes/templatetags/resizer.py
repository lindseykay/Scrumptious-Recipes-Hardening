from django import template

register = template.Library()


def resize_to(ingredient, target):
    serving_size = ingredient.recipe.servings
    if serving_size is not None and target is not None:
        try:
            ratio = int(target) / int(serving_size) * ingredient.amount
            return ratio
        except Exception:
            pass
    else:
        return ingredient.amount


register.filter(resize_to)
