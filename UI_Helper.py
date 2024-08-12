HEADER = 'Welcome To Grocery Lister'

def print_header():
    print('\n')
    print('*********************************')
    print(f'****{HEADER}****')
    print('*********************************')
    print('\n')


def print_commands(commands):
    command_list = '|'
    for command in commands:
        command_list += command + '|'
    print(command_list)


def print_grocery_list(grocery_list):
    print("______________")
    print("You will need:")
    print("______________")
    index = 1
    for item, quantity in grocery_list.items():
        print(f'{index}. {item} x{quantity}')
        index += 1
    print('\n')