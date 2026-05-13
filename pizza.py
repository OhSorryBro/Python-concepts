def make_pizza(size, *toppings):
    """Wrap-up of information about pizza"""
    print(f"\n We are making pizza that is {size}, with following toppings:")
    for topping in toppings:
        print(f" - {topping}")