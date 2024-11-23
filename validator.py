from data.data_service import DataService

class Validator:

    @staticmethod
    def yes_no(response):
        while response not in ['y', 'n']:
            print('Sorry, that is not a valid response')
            response = input('>> ')
        return response

    @staticmethod
    def recipe_selection(response):
        while True:
            try:
                selected_recipes = [int(x) for x in response.split(',')]
                valid_response = True
                for index in selected_recipes:
                    if (index - 1) < 0 or index > len(DataService.get_recipes()):
                        print(f'{index} is not an available option. Please re-enter your list.')
                        response = input('>> ')
                        valid_response = False
                        break
                if valid_response:
                    return selected_recipes
            except ValueError:
                print('Please enter a valid list.')
                response = input('>> ')

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
