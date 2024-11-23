import json
from config.config_service import ConfigService
from validator import Validator


class Recipe:
    def __init__(self):
        self.name = ''
        self.ingredients = {}
        self.cost = 0.00
        self.serving_size = 0

    def set_name(self, name):
        self.name = name

    def add_ingredient(self, ingredient, quantity):
        self.ingredients[ingredient] = quantity

    def set_cost(self, cost):
        self.cost = cost

    def set_serving_size(self, serving_size):
        self.serving_size = serving_size

    def save_recipe(self):
        new_recipe = {
            self.name: {
                'ingredients': self.ingredients,
                'approximate cost': self.cost,
                'serving size': self.serving_size
            }
        }

        with open('data/recipes.json', 'r') as data_file:
            recipes = json.load(data_file)

        recipes.update(new_recipe)
        with open('data/recipes.json', 'w') as data_file:
            json.dump(recipes, data_file, indent=4)
