#IMPORTS
import json

#VARIABLES
HEADER = 'Welcome To Grocery Lister'
COMMANDS = ['create list', 'add recipe', 'exit']
CATEGORIES = ['chicken', 'beef', 'pork', 'fish', 'sausage', 'vegetarian']
grocery_list = {}
exit_program = False

#TODO: Remove Ingredients

#TODO: Import Recipe

#TODO: Order Ingredients


def remove_items():
    print('Which items would you like to remove?')
    items_to_remove = input('>> ').split(',')
    offset = 1
    if '' in items_to_remove:
        pass
    else:
        for index in items_to_remove:
            item = list(grocery_list.keys())[int(index) - offset]
            grocery_list.pop(item)
            offset += 1


def create_grocery_list():
    with open('data/recipes.json', 'r') as data_file:
        recipes = json.load(data_file)

    with open('data/ignore.txt', 'r') as data_file:
        ignore = data_file.read().splitlines()

    print("Please select which recipes to add to the grocery list:\n")
    index = 1
    for recipe in recipes.keys():
        print(f'{index}. {recipe} (serving size: {recipes[recipe]['serving size']}) - ${recipes[recipe]['approximate cost']}/meal')
        index += 1

    chosen_recipes = input('>> ').split(',')
    for index in chosen_recipes:
        recipe = list(recipes.keys())[int(index) - 1]
        for ingredient, quantity, in recipes[recipe]["ingredients"].items():
            if ingredient in ignore:
                pass
            elif ingredient in grocery_list:
                grocery_list[ingredient] += quantity
            else:
                grocery_list[ingredient] = quantity


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


def print_grocery_list():
    print("______________")
    print("You will need:")
    print("______________")
    index = 1
    for ingredient, quantity in grocery_list.items():
        print(f'{index}. {ingredient} x{quantity}')
        index += 1
    print('\n')


print_header()

#Main Loop
while not exit_program:
    print_commands()
    match input('>> '):
        case 'create list':
            create_grocery_list()
            print_grocery_list()
            remove_items()
            print_grocery_list()
        case 'add recipe':
            pass
        case 'exit':
            exit_program = True
        case _:
            print("sorry that is not a command")
