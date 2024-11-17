import json
from config.config_service import ConfigService

cs = ConfigService()


class GroceryList:
    def __init__(self):
        self.items = {}

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
