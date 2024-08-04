#IMPORTS
import json

#VARIABLES
HEADER = 'Welcome To Grocery Lister'
COMMANDS = ['create list', 'create recipe', 'help', 'exit']
CATEGORIES = ['chicken', 'beef', 'pork', 'fish', 'sausage', 'vegetarian']
grocery_list = []
exit_program = False

#TODO: Display Grocery List
def print_list():
    for food in grocery_list:
        print(food)

def print_commands():
    for command in COMMANDS:
        print(command)

#TODO: Add Item To Grocery List
def add_item():
    grocery_list.append(input("what item do you want to add >>"))

def get_recipes():
    with open('data/recipes.json', 'r') as data_file:
        recipes = json.load(data_file)

        print("Please select which recipes to add to the grocery list:\n")
        index = 1;
        for recipe in recipes.keys():
            print(f'{index}. {recipe} (serving size: {recipes[recipe]['serving size']}) - ${recipes[recipe]['approximate cost']}/meal')
            index += 1

        response = input('>> ')
        chosen_recipes = response.split(',')

        print("______________")
        print("You will need:")
        print("______________")

        for index in chosen_recipes:
            recipe = list(recipes.keys())[int(index) - 1]
            for ingredient,quantity in recipes[recipe]["ingredients"].items():
                print(f'{ingredient} x{quantity}')


def create_grocery_list():
    pass

def print_header():
    print('\n')
    print('*********************************')
    print(f'****{HEADER}****')
    print('*********************************')
    print('\n')

print_header()
get_recipes()

#TODO: Main Loop
while not exit_program:

    match input('>> '):
        case 'create list':
            create_grocery_list()
        case 'create recipe':
            pass
        case 'help':
            print_commands()
        case 'exit':
            exit_program = True
        case _:
            print("sorry that is not a command")
