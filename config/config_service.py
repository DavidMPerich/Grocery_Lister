import json
from validator import Validator


class ConfigService:
    @staticmethod
    def add_category(category, ingredient):
        with open('config/category_lookup.json', 'r') as data_file:
            cat_lookup = json.load(data_file)

        cat_lookup[ingredient] = category

        with open('config/category_lookup.json', 'w') as data_file:
            json.dump(cat_lookup, data_file, indent=4)

    @staticmethod
    def get_items():
        with open('config/category_lookup.json') as data_file:
            ingredients = sorted(list(json.load(data_file).keys()))
        return ingredients

    @staticmethod
    def get_ignore_cases():
        with open('config/ignore.txt', 'r') as data_file:
            ignore_cases = data_file.read().splitlines()
        return ignore_cases

    @staticmethod
    def get_sections():
        with open('config/layout.json', 'r') as data_file:
            layout = json.load(data_file)
        sections = []
        for aisle in layout:
            sections += layout[aisle]
        return sections

    @staticmethod
    def get_section(item):
        with open('config/category_lookup.json', 'r') as data_file:
            cat_lookup = json.load(data_file)
        return cat_lookup[item]
