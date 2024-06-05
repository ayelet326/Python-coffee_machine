from menu import Menu, MenuItem


class CoffeeMaker:
    """Models the machine that makes the coffee"""

    def __init__(self):
        self.resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100,
        }

    def report(self):
        """Prints a report of all resources."""
        print(f"Water :{self.resources['water']}\nMilk :{self.resources['milk']}\nCoffee :{self.resources['coffee']}\n")

    def is_resource_sufficient(self, drink):
        """Returns True when order can be made, False if ingredients are insufficient."""
        newMenu = Menu()
        ingredients = newMenu.find_drink(drink)
        for k, v in self.resources.items():
            if ingredients.ingredients[k] > v:
                print(f"sorry there is no enough {k}")
                return False
        return True

    def make_coffee(self, order):
        """Deducts the required ingredients from the resources."""
        newMenu = Menu()
        ingredients = newMenu.find_drink(order)
        for k, v in ingredients.ingredients.items():
            self.resources[k] -= v

        print(f"Here is your {ingredients.name} ☕️. Enjoy!")
