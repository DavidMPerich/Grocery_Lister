from grocery_list import GroceryList
from recipe import Recipe
from config.config_service import ConfigService
from data.data_service import DataService
from validator import Validator

TEST_MODE = False
HEADER = 'Welcome To Grocery Lister'
COMMANDS = ['create list', 'add recipe', 'search', 'test', 'exit']
GROUPS = ['Chicken', 'Beef', 'Vegetarian', 'Seafood', 'Sausage']
exit_program = False

#TODO: Add Website Link to Recipe


def print_header():
    print('\n')
    print('*********************************')
    print(f'****{HEADER}****')
    print('*********************************')
    print('\n')


def print_commands():
    command_list = '|'
    for command in COMMANDS:
        command_list += command + '|'
    print(command_list)


def index_list(list_to_print):
    index = 1
    for item in list_to_print:
        print(f'{index}. {item}')
        index += 1


def select_category(item):
    if item not in ConfigService.get_items():
        categories = sorted(ConfigService.get_sections())
        size = len(categories)

        index_list(categories)
        print('Which category does this belong to?')
        response = Validator.category(input('>> '), size)
        ConfigService.add_category(categories[response - 1], item)


def create_list():
    grocery_list = GroceryList()
    available_recipes = DataService.get_recipes()
    size = len(available_recipes)

    index_list(available_recipes)
    print('\nPlease select which recipes to add to the grocery list:')
    response = Validator.recipe_selection(input('>> '), size)

    for index in response:
        selected_recipe = available_recipes[index - 1]
        ingredients = DataService.get_ingredients(selected_recipe)
        grocery_list.add_recipe_ingredients(ingredients)

    grocery_list.print_items()

    print('Would you like to remove any items? (y/n)')
    response = Validator.yes_no(input('>> '))

    if response == 'y':
        print('Which items would you like to remove? (e.g. item - quantity)')
        response = input('>> ')

        while response:
            (item, quantity) = Validator.ingredient_quantity(response)
            grocery_list.remove_item(item, quantity)
            response = input('>> ')

        grocery_list.print_items()

    print('Would you like to add any items? (y/n)')
    response = Validator.yes_no(input('>> '))

    if response == 'y':
        for item in ConfigService.get_items():
            print(item)

        print('Which items do you want to add? (e.g. item - quantity)')
        response = input('>> ')

        while response:
            (item, quantity) = Validator.ingredient_quantity(response)
            if item not in ConfigService.get_items():
                select_category(item)
            grocery_list.add_item(item, quantity)
            response = input('>> ')

    grocery_list.order_items()
    grocery_list.print_items()


def add_recipe():
    recipe = Recipe()

    print('What is the name of the recipe?')
    name = input('>> ').title()
    recipe.set_name(name)

    index_list(GROUPS)
    size = len(GROUPS)
    print('What type of recipe is it?')
    response = Validator.group(input('>> '), size)
    recipe.set_group(GROUPS[response - 1])

    print('What are the ingredients? (e.g. item - quantity)')
    response = input('>> ')
    while response:
        (ingredient, quantity) = Validator.ingredient_quantity(response)
        if ingredient not in ConfigService.get_items():
            select_category(ingredient)
        recipe.add_ingredient(ingredient, quantity)
        response = input('>> ')

    print('How much does this recipe cost?')
    cost = Validator.cost(input('>> '))
    recipe.set_cost(cost)

    print('How many does this recipe serve?')
    serving_size = Validator.serving_size(input('>> '))
    recipe.set_serving_size(serving_size)

    recipe.save_recipe()


def search_by_group():
    index_list(GROUPS)
    size = len(GROUPS)
    print('Which recipes would you like to view?')
    response = Validator.group(input('>> '), size)
    group = GROUPS[response - 1]
    recipes = DataService.get_recipes_by_group(group)
    for recipe in recipes:
        print(recipe)


def search_by_ingredient():
    available_items = ConfigService.get_items()
    for item in available_items:
        print(item)
    print('Which ingredient would you like to search for?')
    response = input('>> ').lower()
    if response not in available_items:
        print(f'No recipes contain {response}')
    else:
        recipes = DataService.get_recipes_by_ingredient(response)
        for recipe in recipes:
            print(recipe)


def test():
    pass


if TEST_MODE:
    test()
    exit()

print_header()
#Main Loop
while not exit_program:
    print_commands()
    match input('>> '):
        case 'create list':
            create_list()
        case 'add recipe':
            add_recipe()
        case 'search':
            print('What would you like to search by?')
            print('|group|ingredient|')
            while True:
                match input('>> '):
                    case 'group':
                        search_by_group()
                        break
                    case 'ingredient':
                        search_by_ingredient()
                        break
                    case _:
                        print('Sorry, that is not an option')
        case 'test':
            test()
        case 'exit':
            exit_program = True
        case _:
            print('Sorry, that is not a command')
