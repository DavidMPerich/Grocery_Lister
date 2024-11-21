import json
from config.config_service import ConfigService

cs = ConfigService()


class Recipe:
    def __init__(self):
        self.name = ""
        self.ingredients = {}
        self.cost = 0.00
        self.serving_size = 0

    def set_name(self, name):
        self.name = name

    def add_ingredients(self, ingredients):
        segments = ingredients.split(' - ')
        ingredient = segments[0]

        if len(segments) > 1:
            quantity = int(segments[1])
        else:
            #TODO: Add Validation
            print('How many?')
            quantity = int(input('>>'))

        if ingredient not in ConfigService.get_items():
            ConfigService.add_category(ConfigService.select_category(), ingredient)

        self.ingredients[ingredient] = quantity

    def set_cost(self, cost):
        self.cost = cost

    def set_serving_size(self, serving_size):
        self.serving_size = serving_size

    def save_recipe(self):
        new_recipe = {
            self.name: {
                "ingredients": self.ingredients,
                "approximate cost": self.cost,
                "serving size": self.serving_size
            }
        }

        with open('data/recipes.json', 'r') as data_file:
            recipes = json.load(data_file)

        recipes.update(new_recipe)
        with open('data/recipes.json', 'w') as data_file:
            json.dump(recipes, data_file, indent=4)
