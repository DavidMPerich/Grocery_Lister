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
