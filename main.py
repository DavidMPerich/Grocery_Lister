#IMPORTS


#VARIABLES
HEADER = 'Welcome To Grocery Lister'
COMMANDS = ['create list', 'create recipe', 'help', 'exit']
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

print(HEADER)


def create_grocery_list():
    pass

#TODO: Main Loop
while not exit_program:
    #response = input(">> ")

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
