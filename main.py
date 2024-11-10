#IMPORTS
from grocery_list import GroceryList
from recipe import Recipe
import json

#VARIABLES
HEADER = 'Welcome To Grocery Lister'
COMMANDS = ['create list', 'add recipe', 'test', 'exit']
OPTIONS = ['import', 'manual']
grocery_list = {}
exit_program = False


#TODO: Import Recipe

#TODO: Make Recipe OO


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


def print_options():
    options_list = "|"
    for option in OPTIONS:
        options_list += option + '|'
    print(options_list)


def add_recipe():
    print("\n\nWould you like to import a recipe or manually add a recipe?")
    print_options()
    match input('>> '):
        case 'import':
            pass
        case 'manual':
            recipe = Recipe()
            recipe.add_name()
            recipe.add_ingredients()
            recipe.add_cost()
            recipe.add_serving_size()
            recipe.save_recipe()
        case _:
            print('sorry that is not an option')


def test():
    pass


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
