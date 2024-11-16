import json
from config.config_service import ConfigService

cs = ConfigService()


class GroceryList:
    def __init__(self):
        self.items = {}

    def add_items(self):
        print('Would you like to add any items? (y/n)')
        match input('>> '):
            case 'y':
                pass
            case 'n':
                return
            case _:
                print('sorry that is not an option')
                self.add_items()

        items = cs.get_items()
        for item in items:
            print(item)

        print('What items do you want to add? (Example: white onion - 1)')
        response = input('>> ')

        while response:
            item = response.split(' - ')[0]
            quantity = int(response.split(' - ')[1])

            if item not in items:
                category = cs.get_category()
                cs.add_category(category, item)

            if item in self.items.keys():
                self.items[item] += quantity
            else:
                self.items[item] = quantity

            response = input('>> ')

        self.print_items()

    def remove_items(self):
        print("Would you like to remove any items? (y/n)")
        response = input('>> ')

        while response == 'y':
            print('Which item would you like to remove?')
            item_to_remove = input('>> ')

            try:
                item = list(self.items.keys())[int(item_to_remove) - 1]
            except IndexError:
                print('That item is not on the list')
                continue

            print('How many would you like to remove?')
            quantity_to_remove = int((input('>> ')))

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
