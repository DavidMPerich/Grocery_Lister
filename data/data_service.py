import json


class DataService:

    @staticmethod
    def get_recipes():
        with open('data/recipes.json', 'r') as data_file:
            recipes = sorted(list(json.load(data_file).keys()))
        return recipes

    @staticmethod
    def get_ingredients(recipe):
        with open('data/recipes.json', 'r') as data_file:
            recipes = json.load(data_file)
        return recipes[recipe]['ingredients']

    @staticmethod
    def get_recipes_by_group(group):
        recipes_to_return = []
        with open('data/recipes.json', 'r') as data_file:
            recipes = json.load(data_file)

        for recipe in recipes:
            if recipes[recipe]['group'] == group:
                recipes_to_return.append(recipe)

        return recipes_to_return

    @staticmethod
    def get_recipes_by_ingredient(ingredient):
        recipes_to_return = []
        with open('data/recipes.json', 'r') as data_file:
            recipes = json.load(data_file)

        for recipe in recipes:
            if ingredient in recipes[recipe]['ingredients'].keys():
                recipes_to_return.append(recipe)

        return recipes_to_return
