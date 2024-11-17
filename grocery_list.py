import json
from config.config_service import ConfigService

cs = ConfigService()


class GroceryList:
    def __init__(self):
        self.items = {}

    def order_items(self):
        ordered_list = {}
        sections = ConfigService.get_sections()

        for section in sections:
            for item, quantity in self.items.items():
                if ConfigService.get_section(item) == section:
                    ordered_list[item] = quantity

        self.items = ordered_list

    def print_items(self):
        print("______________")
        print("You will need:")
        print("______________")
        index = 1
        for item, quantity in self.items.items():
            print(f'{index}. {item} x{quantity}')
            index += 1
        print('\n')
