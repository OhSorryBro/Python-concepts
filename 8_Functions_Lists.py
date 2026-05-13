def greet_users(names):
    """Print simple welcome to every user on the list"""
    for name in names:
        msg = f'Hello, {name.title()}'
        print(msg)

usernames =['hellen', 'tym', 'april']
greet_users(usernames)

unprinted_designs =['phone case', 'robot pendant', 'triangle']
completed_models =[]

while unprinted_designs:
    current_design = unprinted_designs.pop()
    print(f'Printing model: {current_design}')
    completed_models.append(current_design)

print("\n Following models were printed: ")
for completed_model in completed_models:
    print(completed_model)



def print_models(unprinted_designs, completed_models):
    ''' We simulate printing of projects, until there are none to print. Every printed model will be transferred to the list completed_models.'''
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f'Printing model: {current_design}')
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """Shows all models that were printed"""
    print("\n There were printed following models: ")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['phone case', 'robot pendant', 'triangle']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)