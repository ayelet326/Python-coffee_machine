from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
menu = Menu()
money_machine = MoneyMachine()

print("Coffee machine:")
print("off=(to turn of press off )")
off = True
x = input("What would you like?\nespresso\nlatte\ncappuccino\n report\n")
if x == "off":
    off = False
    print("bye bye!!")
while off:

    if x == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        if menu.find_drink(x) is None:
            break
        elif coffee_maker.is_resource_sufficient(x):
            m = money_machine.process_coins()
            if not money_machine.make_payment(menu.find_drink(x).cost):
                print(f"Sorry that's not enough money.Money returnd")
            else:
                coffee_maker.make_coffee(x)

    x = input("What would you like?\nespresso\nlatte\ncappuccino\nreport\n")
    if x == "off":
        off = False
        print("bye bye!!")
