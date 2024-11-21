#IMPORTS
from grocery_list import GroceryList
from recipe import Recipe
from config.config_service import ConfigService
from data.data_service import DataService


#VARIABLES
TEST_MODE = False
HEADER = 'Welcome To Grocery Lister'
COMMANDS = ['create list', 'add recipe', 'test', 'exit']
exit_program = False
VALID_RESPONSES = ['y', 'n']


#TODO: Search Recipe By Ingredient

#TODO: Categorize Recipes

#TODO: Add Website Link to Recipe

#TODO: Add Price to Ingredients to Determine Cost

#TODO: Verify Prompt Comes After List

#TODO: Verify Single v Double Quotes

#TODO: Print v Text

#TODO: Add/Remove Items Convert from Int to Float

def print_header():
    print('\n')
    print('*********************************')
    print(f'****{HEADER}****')
    print('*********************************')
    print('\n')


def validate_response(response):
    while response not in VALID_RESPONSES:
        print('Sorry, that is not a valid response')
        response = input('>> ')
    return response


def validate_recipe_selection(index, recipe_list):
    while (index - 1) < 0 or index > len(recipe_list):
        print(f'{index} is not an option. Please choose another')
        index = int(input('>> '))
    return index


def print_commands():
    command_list = '|'
    for command in COMMANDS:
        command_list += command + '|'
    print(command_list)


def create_list():
    grocery_list = GroceryList()

    index = 1
    available_recipes = DataService.get_recipes()

    # ADD RECIPES
    for recipe in available_recipes:
        print(f'{index}. {recipe}')
        index += 1
    print('\nPlease select which recipes to add to the grocery list:')
    selected_recipes = [int(x) for x in input('>> ').split(',')]

    for index in selected_recipes:
        index = validate_recipe_selection(index, available_recipes)
        grocery_list.add_recipe_ingredients(index)

    grocery_list.print_items()

    #REMOVE ITEMS
    print('Would you like to remove any items? (y/n)')
    response = validate_response(input('>> '))

    if response == 'y':
        print('Which items would you like to remove?')
        response = input('>> ')

        while response:
            grocery_list.remove_item(response)
            response = input('>> ')

        grocery_list.print_items()

    #ADD ITEMS
    print('Would you like to add any items? (y/n)')
    response = validate_response(input('>> '))

    if response == 'y':
        for item in ConfigService.get_items():
            print(item)

        print('Which items do you want to add?')
        response = input('>> ')

        while response:
            grocery_list.add_item(response)
            response = input('>> ')

    #ORDER LIST
    grocery_list.order_items()
    grocery_list.print_items()


def add_recipe():
    recipe = Recipe()
    items = ConfigService.get_items()

    print('What is the name of the recipe?')
    recipe.name = input('>> ').title()

    print('What are the ingredients?')
    response = input('>> ')
    while response:
        segments = response.split(' - ')
        ingredient = segments[0]
        if len(segments) > 1:
            quantity = int(segments[1])
        else:
            print('How many?')
            quantity = int(input('>> '))

        if ingredient not in items:
            ConfigService.add_category(ConfigService.select_category(), ingredient)

        recipe.ingredients[ingredient] = quantity
        response = input('>> ')

    print('How much does this recipe cost?')
    recipe.cost = float(input('>> '))

    print('How many does this recipe serve?')
    recipe.serving_size = int(input('>> '))

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
            print("Sorry, that is not a command")
