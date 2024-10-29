import json


class GroceryList:
    def __init__(self):
        self.items = {}

    def add_recipes(self):
        with open('data/recipes.json', 'r') as data_file:
            recipes = json.load(data_file)

        with open('config/ignore.txt', 'r') as data_file:
            ignore = data_file.read().splitlines()

        print("Please select which recipes to add to the grocery list:\n")
        index = 1
        for recipe in recipes.keys():
            print(
                f'{index}. {recipe} (serving size: {recipes[recipe]['serving size']}) - ${recipes[recipe]['approximate cost']}/meal')
            index += 1

        chosen_recipes = input('>> ').split(',')
        for index in chosen_recipes:
            recipe = list(recipes.keys())[int(index) - 1]
            for ingredient, quantity, in recipes[recipe]["ingredients"].items():
                if ingredient in ignore:
                    pass
                elif ingredient in self.items:
                    self.items[ingredient] += quantity
                else:
                    self.items[ingredient] = quantity

        self.print_items()

    def add_items(self):
        print("Would you like to add any items? (y/n)")
        response = input('>> ')

        with open('data/additions.txt', 'r') as data_file:
            additions = data_file.read().splitlines()

        index = 1
        for item in additions:
            print(f'{index}. {item}')
            index += 1

        while response == 'y':
            print('Which item would you like to add?')
            item_to_add = input('>> ')
            print('How many would you like to add?')
            quantity_to_add = int(input('>> '))
            item = additions[int(item_to_add) - 1]
            if item_to_add in self.items.keys():
                self.items[item] += quantity_to_add
            else:
                self.items[item] = quantity_to_add
            print('Would you like to add any more items? (y/n)')
            response = input('>> ')

        self.print_items()

    def remove_items(self):
        print("Would you like to remove any items? (y/n)")
        response = input('>> ')

        while response == 'y':
            print('Which item would you like to remove?')
            item_to_remove = input('>> ')
            print('How many would you like to remove?')
            quantity_to_remove = int((input('>> ')))
            # TODO: Make sure item is in the list
            item = list(self.items.keys())[int(item_to_remove) - 1]
            if self.items[item] == quantity_to_remove:
                self.items.pop(item)
            elif self.items[item] > quantity_to_remove:
                self.items[item] -= quantity_to_remove
            else:
                print('You do not have that many to remove')
            print('Would you like to remove any more items? (y/n)')
            response = input('>> ')

        self.print_items()

    def order_items(self):
        with open('config/layout.json', 'r') as data_file:
            layout = json.load(data_file)

        with open('config/category_lookup.json', 'r') as data_file:
            categories = json.load(data_file)

        index = 1
        for aisle in list(layout.keys()):
            display_aisle = True
            for section in layout[aisle]:
                for item, quantity in self.items.items():
                    if categories[item] == section:
                        if display_aisle:
                            print(aisle.upper())
                            display_aisle = False
                        print(f'{index}. {item} x{quantity}')
                        index += 1

    def print_items(self):
        print("______________")
        print("You will need:")
        print("______________")
        index = 1
        for item, quantity in self.items.items():
            print(f'{index}. {item} x{quantity}')
            index += 1
        print('\n')
