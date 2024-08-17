#IMPORTS
from UI_Helper import print_header, print_commands
from grocery_list import GroceryList

#VARIABLES
COMMANDS = ['create list', 'add recipe', 'exit']
grocery_list = {}
exit_program = False
grocery_list = GroceryList()

#TODO: Add Ingredients

#TODO: Import Recipe

#TODO: Order Ingredients

#TODO: Make Recipe OO

print_header()

#Main Loop
while not exit_program:
    print_commands(COMMANDS)
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
