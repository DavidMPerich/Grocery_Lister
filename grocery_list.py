import json
from config.config_service import ConfigService

#TODO: Refactor to remove ConfigService if possible


class GroceryList:
    def __init__(self):
        self.items = {}

    def add_recipe_ingredients(self, ingredients):
        for ingredient, quantity in ingredients.items():
            if ingredient in ConfigService.get_ignore_cases():
                pass
            elif ingredient in self.items:
                self.items[ingredient] += quantity
            else:
                self.items[ingredient] = quantity

    def order_items(self):
        ordered_list = {}
        sections = ConfigService.get_sections()

        for section in sections:
            for item, quantity in self.items.items():
                if ConfigService.get_section(item) == section:
                    ordered_list[item] = quantity

        self.items = ordered_list

    def print_items(self):
        print('______________')
        print('You will need:')
        print('______________')
        index = 1
        for item, quantity in self.items.items():
            print(f'{index}. {item} x{quantity}')
            index += 1
        print('\n')

    def remove_item(self, item, quantity):
        while item not in self.items:
            print('Sorry, that item is not on the list')
            item = input('>> ').split(' - ')[0]

        if self.items[item] == quantity:
            self.items.pop(item)
        elif self.items[item] > quantity:
            self.items[item] -= quantity
        else:
            print('You do not have that many to remove')

    def add_item(self, item, quantity):
        if item not in ConfigService.get_items():
            ConfigService.add_category(ConfigService.select_category(), item)

        if item in self.items.keys():
            self.items[item] += quantity
        else:
            self.items[item] = quantity
