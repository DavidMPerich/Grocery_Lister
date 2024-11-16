#IMPORTS
from grocery_list import GroceryList
from recipe import Recipe
from config.config_service import ConfigService
from data.data_service import DataService


#VARIABLES
TEST_MODE = True
HEADER = 'Welcome To Grocery Lister'
COMMANDS = ['create list', 'add recipe', 'test', 'exit']
exit_program = False


#TODO: Search Recipe By Ingredient

#TODO: Categorize Recipes

#TODO: Add Website Link to Recipe

#TODO: Add Price to Ingredients to Determine Cost

#TODO: Verify Prompt Comes After List

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
    ignore_cases = ConfigService.get_ignore_cases()

    for recipe in available_recipes:
        print(f'{index}. {recipe}')
        index += 1

    print('\nPlease select which recipes to add to the grocery list:')
    selected_recipes = input('>> ').split(',')

    for index in selected_recipes:
        recipe = available_recipes[int(index) - 1]
        ingredients = DataService.get_ingredients(recipe)
        for ingredient, quantity in ingredients.items():
            if ingredient in ignore_cases:
                pass
            elif ingredient in grocery_list.items:
                grocery_list.items[ingredient] += quantity
            else:
                grocery_list.items[ingredient] = quantity

    grocery_list.print_items()

    #TODO: Continue Here
    grocery_list.remove_items()
    grocery_list.add_items()
    grocery_list.order_items()


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
            ConfigService.add_category(ConfigService.get_category(), ingredient)

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
            print("sorry that is not a command")
