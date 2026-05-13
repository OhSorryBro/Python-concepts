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