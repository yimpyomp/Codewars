# https://www.codewars.com/kata/525c65e51bf619685c000059/train/python


def cakes(recipe, available):
    ingredient_limits = []
    for key in recipe.keys():
        if key not in available.keys():
            return 0
        else:
            ingredient_limits.append(available[key] // recipe[key])
    return min(ingredient_limits)

