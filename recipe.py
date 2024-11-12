import json
from config.config_service import ConfigService

cs = ConfigService()


class Recipe:
    def __init__(self):
        self.name = ""
        self.ingredients = {}
        self.cost = 0.00
        self.serving_size = 0

    def add_name(self):
        print('What is the name of the recipe?')
        self.name = input('>> ').title()

    def add_ingredients(self):
        with open('config/category_lookup.json', 'r') as data_file:
            ingredients = json.load(data_file)

        print('What are the ingredients? (Example: white onion - 1)')
        response = input('>> ')

        while response:
            #TODO: Error Handling For Correct Format
            ingredient = response.split(' - ')[0]
            quantity = int(response.split(' - ')[1])

            if ingredient not in ingredients:
                category = cs.get_category()
                ConfigService.add_category(self, category, ingredient)

            self.ingredients[ingredient] = quantity
            response = input('>> ')


    def add_cost(self):
        print('How much does this recipe cost approximately?')
        self.cost = float(input('>> '))

    def add_serving_size(self):
        print('How many does this recipe serve?')
        self.serving_size = int(input('>> '))

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
