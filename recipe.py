import json


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
        response = 'y'

        while response == 'y':
            print('Which ingredient would you like to add?')
            ingredient_to_add = input('>> ').lower()
            print('How many would you like to add?')
            quantity_to_add = int(input('>> '))
            self.ingredients[ingredient_to_add] = quantity_to_add
            print('Would you like to add any more ingredients? (y/n)')
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
