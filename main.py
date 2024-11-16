#IMPORTS
from grocery_list import GroceryList
from recipe import Recipe
from config.config_service import ConfigService


#VARIABLES
TEST_MODE = False
HEADER = 'Welcome To Grocery Lister'
COMMANDS = ['create list', 'add recipe', 'test', 'exit']
grocery_list = {}
cs = ConfigService()
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


def add_recipe():
    recipe = Recipe()
    items = cs.get_items()

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
            cs.add_category(cs.get_category(), ingredient)

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
            grocery_list = GroceryList()
            grocery_list.add_recipes()
            grocery_list.remove_items()
            grocery_list.add_items()
            grocery_list.order_items()
            exit_program = True
        case 'add recipe':
            add_recipe()
        case 'test':
            test()
        case 'exit':
            exit_program = True
        case _:
            print("sorry that is not a command")
