import json


class ConfigService:

    def get_category(self):
        with open('config/layout.json', 'r') as data_file:
            layout = json.load(data_file)

        categories = []
        index = 1

        print('Which category does this belong in?')
        for aisle in layout:
            categories += layout[aisle]

        categories = sorted(categories)
        for category in categories:
            print(f'{index}. {category}')
            index += 1

        response = int(input('>> '))
        return categories[response - 1]

    def add_category(self, category, ingredient):
        with open('config/category_lookup.json', 'r') as data_file:
            cat_lookup = json.load(data_file)

        cat_lookup[ingredient] = category

        with open('config/category_lookup.json', 'w') as data_file:
            json.dump(cat_lookup, data_file, indent=4)