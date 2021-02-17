from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

# Turn the machine On
isOn = True

while isOn:
    user_input = input("What would you like? (espresso/latte/cappuccino): ")
    if user_input == 'off':
        # Turn Machine Off
        isOn = False
        continue
    if user_input == 'report':
        # Print machine report
        coffee_maker.report()
        money_machine.report()
        continue
    else:
        # See if user input is on the menu
        order = menu.find_drink(user_input)
        if order:
            # See if machine has sufficient resources to make requested drink
            if coffee_maker.is_resource_sufficient(order):
                # Attempt to make purchase
                if money_machine.make_payment(order.cost):
                    # Make the order
                    coffee_maker.make_coffee(order)
                else:
                    continue
            else:
                continue

