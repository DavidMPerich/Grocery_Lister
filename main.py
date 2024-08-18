#IMPORTS
from grocery_list import GroceryList

#VARIABLES
HEADER = 'Welcome To Grocery Lister'
COMMANDS = ['create list', 'add recipe', 'exit']
grocery_list = {}
exit_program = False
grocery_list = GroceryList()

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


print_header()

#Main Loop
while not exit_program:
    print_commands()
    match input('>> '):
        case 'create list':
            grocery_list.add_recipes()
            grocery_list.remove_items()
            grocery_list.add_items()
            grocery_list.order_items()
            exit_program = True
        case 'add recipe':
            pass
        case 'exit':
            exit_program = True
        case _:
            print("sorry that is not a command")
