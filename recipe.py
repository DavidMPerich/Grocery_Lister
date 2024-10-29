import json


class Recipe:
    def __init__(self):
        self.name = ""
        self.ingredients = {}
        self.cost = 0.00
        self.serving_size = 0

    def add_name(self):
        print('What is the name of the recipe?')
        self.name = input('>> ')

    def add_ingredients(self):
        response = 'y'

        while response == 'y':
            print('Which ingredient would you like to add?')
            ingredient_to_add = input('>> ')
            print('How many would you like to add?')
            quantity_to_add = int(input('>> '))
            self.ingredients[ingredient_to_add] = quantity_to_add
            print('Would you like to add any more ingredients? (y/n)')
            response = input('>> ')

        print(self.ingredients)

    def add_cost(self):
        pass

    def add_serving_size(self):
        pass
