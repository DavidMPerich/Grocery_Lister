#IMPORTS
import json

#VARIABLES
HEADER = 'Welcome To Grocery Lister'
COMMANDS = ['create list', 'add recipe', 'exit']
CATEGORIES =
grocery_list = {}
exit_program = False

#TODO: Add Ingredients

#TODO: Import Recipe

#TODO: Order Ingredients


def remove_items():
    print("Would you like to remove any items? (y/n)")
    response = input('>> ')

    while response == 'y':
        print('Which item would you like to remove?')
        item_to_remove = input('>> ')
        print('How many would you like to remove?')
        quantity_to_remove = int((input('>> ')))
        item = list(grocery_list.keys())[int(item_to_remove) - 1]
        if grocery_list[item] == quantity_to_remove:
            grocery_list.pop(item)
        elif grocery_list[item] > quantity_to_remove:
            grocery_list[item] -= quantity_to_remove
        else:
            print('You do not have that many to remove')
        print('Would you like to remove any more items? (y/n)')
        response = input('>> ')


def create_grocery_list():
    with open('data/recipes.json', 'r') as data_file:
        recipes = json.load(data_file)

    with open('config/ignore.txt', 'r') as data_file:
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
