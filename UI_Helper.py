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
