import json


class ConfigService:

    #TODO: Remove Any Unnecessary IO

    @staticmethod
    def get_category():
        with open('config/layout.json', 'r') as data_file:
            layout = json.load(data_file)

        categories = []
        index = 1

        #TODO: Make Easier To Select Category
        print('Which category does this belong in?')
        for aisle in layout:
            categories += layout[aisle]

        categories = sorted(categories)
        for category in categories:
            print(f'{index}. {category}')
            index += 1

        response = int(input('>> '))
        return categories[response - 1]

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
