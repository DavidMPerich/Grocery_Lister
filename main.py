from grocery_list import GroceryList
from recipe import Recipe
from config.config_service import ConfigService
from data.data_service import DataService
from validator import Validator

TEST_MODE = False
HEADER = 'Welcome To Grocery Lister'
COMMANDS = ['create list', 'add recipe', 'test', 'exit']
exit_program = False

#TODO: Search Recipe By Ingredient

#TODO: Categorize Recipes

#TODO: Add Website Link to Recipe

#TODO: Add Price to Ingredients to Determine Cost


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


def create_list():
    grocery_list = GroceryList()

    index = 1
    available_recipes = DataService.get_recipes()

    for recipe in available_recipes:
        print(f'{index}. {recipe}')
        index += 1
    print('\nPlease select which recipes to add to the grocery list:')
    response = Validator.recipe_selection(input('>> '))

    for index in response:
        selected_recipe = DataService.get_recipes()[index - 1]
        ingredients = DataService.get_ingredients(selected_recipe)
        grocery_list.add_recipe_ingredients(ingredients)

    grocery_list.print_items()

    print('Would you like to remove any items? (y/n)')
    response = Validator.yes_no(input('>> '))

    if response == 'y':
        print('Which items would you like to remove? (e.g. item - quantity)')
        response = input('>> ')

        while response:
            (item, quantity) = Validator.ingredient(response)
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
            (item, quantity) = Validator.ingredient(response)
            grocery_list.add_item(item, quantity)
            response = input('>> ')

    grocery_list.order_items()
    grocery_list.print_items()


def add_recipe():
    recipe = Recipe()
    items = ConfigService.get_items()

    print('What is the name of the recipe?')
    name = input('>> ').title()
    recipe.set_name(name)

    print('What are the ingredients? (e.g. item - quantity)')
    response = input('>> ')
    while response:
        (ingredient, quantity) = Validator.ingredient(response)
        recipe.add_ingredient(ingredient, quantity)
        response = input('>> ')

    print('How much does this recipe cost?')
    cost = Validator.cost(input('>> '))
    recipe.set_cost(cost)

    print('How many does this recipe serve?')
    serving_size = Validator.serving_size(input('>> '))
    recipe.set_serving_size(serving_size)

    recipe.save_recipe()


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
        case 'test':
            test()
        case 'exit':
            exit_program = True
        case _:
            print('Sorry, that is not a command')
