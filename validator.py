class Validator:

    @staticmethod
    def yes_no(response):
        while response not in ['y', 'n']:
            print('Sorry, that is not a valid response')
            response = input('>> ')
        return response

    @staticmethod
    def recipe_selection(index, recipe_list):
        while (index - 1) < 0 or index > len(recipe_list):
            print(f'{index} is not an option. Please choose another')
            index = int(input('>> '))
        return index

    @staticmethod
    def cost(response):
        while True:
            try:
                cost = float(response)
                return cost
            except ValueError:
                print(f'Please enter a valid price')
                response = input('>> ')

    @staticmethod
    def serving_size(response):
        while True:
            try:
                serving_size = int(response)
                return serving_size
            except ValueError:
                print(f'Please enter a valid number')
                response = input('>> ')

    @staticmethod
    def ingredient(response):
        segments = response.split(' - ')

        while True:
            try:
                ingredient = segments[0]
                quantity = int(segments[1])
                return ingredient, quantity
            except ValueError:
                print('Please enter a valid quantity')
                segments = input('>> ').split(' - ')
            except IndexError:
                print('Please include the quantity')
                segments = input('>> ').split(' - ')
