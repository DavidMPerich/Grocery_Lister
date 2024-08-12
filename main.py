#IMPORTS
from UI_Helper import print_header, print_commands, print_grocery_list
import json

#VARIABLES
COMMANDS = ['create list', 'add recipe', 'exit']
grocery_list = {}
exit_program = False

#TODO: Add Ingredients

#TODO: Import Recipe

#TODO: Order Ingredients

#TODO: Refactor


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


def remove_items():
    print("Would you like to remove any items? (y/n)")
    response = input('>> ')

    while response == 'y':
        print('Which item would you like to remove?')
        item_to_remove = input('>> ')
        print('How many would you like to remove?')
        quantity_to_remove = int((input('>> ')))
        #TODO: Make sure item is in the list
        item = list(grocery_list.keys())[int(item_to_remove) - 1]
        if grocery_list[item] == quantity_to_remove:
            grocery_list.pop(item)
        elif grocery_list[item] > quantity_to_remove:
            grocery_list[item] -= quantity_to_remove
        else:
            print('You do not have that many to remove')
        print('Would you like to remove any more items? (y/n)')
        response = input('>> ')


def add_items():
    print("Would you like to add any items? (y/n)")
    response = input('>> ')

    with open('data/additions.txt', 'r') as data_file:
        additions = data_file.read().splitlines()

    index = 1
    for item in additions:
        print(f'{index}. {item}')
        index += 1

    while response == 'y':
        print('Which item would you like to add?')
        item_to_add = input('>> ')
        print('How many would you like to add?')
        quantity_to_add = int((input('>> ')))
        item = additions[int(item_to_add) - 1]
        if item_to_add in grocery_list.keys():
            grocery_list[item] += quantity_to_add
        else:
            grocery_list[item] = quantity_to_add
        print('Would you like to add any more items? (y/n)')
        response = input('>> ')


def order_grocery_list():
    with open('config/layout.json', 'r') as data_file:
        layout = json.load(data_file)

    with open('config/category_lookup.json', 'r') as data_file:
        categories = json.load(data_file)

    index = 1
    for aisle in list(layout.keys()):
        display_aisle = True
        for section in layout[aisle]:
            for item, quantity in grocery_list.items():
                if categories[item] == section:
                    if display_aisle:
                        print(aisle.upper())
                        display_aisle = False
                    print(f'{index}. {item} x{quantity}')
                    index += 1


print_header()

#Main Loop
while not exit_program:
    print_commands(COMMANDS)
    match input('>> '):
        case 'create list':
            create_grocery_list()
            print_grocery_list(grocery_list)
            remove_items()
            print_grocery_list(grocery_list)
            add_items()
            print_grocery_list(grocery_list)
            order_grocery_list()
            exit_program = True
        case 'add recipe':
            pass
        case 'exit':
            exit_program = True
        case _:
            print("sorry that is not a command")

