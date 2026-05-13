def make_pizza(*toppings):
    """Printing list of toppings chosen by the customer"""
    print(toppings)

make_pizza('pepperoni')
make_pizza('muschroms', 'paprika', 'onion')


def make_pizza(*toppings):
    """ Wrap-up of information about pizza"""
    print("\n I am making pizza with following toppings: ")
    for topping in toppings:
        print(f"- {topping}")

make_pizza('pepperoni')
make_pizza('muschroms', 'paprika', 'onion')

def make_pizza(size, *toppings):
    """ Wrap-up of information about pizza"""
    print(f"Making {size} pizza, with following toppings: ")
    for topping in toppings:
        print(f"- {topping}")

make_pizza('16 cm', 'pepperoni')
make_pizza('30 cm', 'muschroms', 'paprika', 'onion')

def build_profile (first, last, **user_info):
    """Building dictionary containing all user information."""
    user_info['first name'] = first
    user_info['last name'] = last
    return user_info

user_profile = build_profile('albert', 'einstein', location ='princeton', field = 'physics')

print(user_profile)