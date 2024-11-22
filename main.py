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


def validate_yes_no(response):
    while response not in VALID_RESPONSES:
        print('Sorry, that is not a valid response')
        response = input('>> ')
    return response


def validate_recipe_selection(index, recipe_list):
    while (index - 1) < 0 or index > len(recipe_list):
        print(f'{index} is not an option. Please choose another')
        index = int(input('>> '))
    return index


def validate_ingredient(response):
    segments = response.split(' - ')

    while True:
        try:
            quantity = int(segments[1])
            return segments[0], int(segments[1])
        except ValueError:
            print('Please enter a valid quantity')
            segments = input('>> ').split(' - ')
        except IndexError:
            print('Please include the quantity')
            segments = input('>> ').split(' - ')


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
        selected_recipe = DataService.get_recipes()[index - 1]
        ingredients = DataService.get_ingredients(selected_recipe)
        grocery_list.add_recipe_ingredients(ingredients)

    grocery_list.print_items()

    #REMOVE ITEMS
    print('Would you like to remove any items? (y/n)')
    response = validate_yes_no(input('>> '))

    if response == 'y':
        print('Which items would you like to remove?')
        response = input('>> ')

        while response:
            grocery_list.remove_item(response)
            response = input('>> ')

        grocery_list.print_items()

    #ADD ITEMS
    print('Would you like to add any items? (y/n)')
    response = validate_yes_no(input('>> '))

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
    name = input('>> ').title()
    recipe.set_name(name)

    print('What are the ingredients?')
    response = input('>> ')
    while response:
        (ingredient, quantity) = validate_ingredient(response)
        recipe.add_ingredient(ingredient, quantity)
        response = input('>> ')

    print('How much does this recipe cost?')
    cost = float(input('>> '))
    recipe.set_cost(cost)

    print('How many does this recipe serve?')
    serving_size = int(input('>> '))
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
            print("Sorry, that is not a command")
