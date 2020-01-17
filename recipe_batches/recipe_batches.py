#!/usr/bin/python

import math


def recipe_batches(recipe, ingredients):
    current_min = float("inf")

    if len(ingredients.keys()) != len(recipe.keys()):
        return 0

    for ing in ingredients.keys():
        if ingredients[ing] // recipe[ing] < current_min:
            current_min = ingredients[ing] // recipe[ing]
    return current_min


if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 50, 'flour': 5}
    ingredients = {'milk': 132, 'butter': 48, 'flour': 51}
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
        batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
