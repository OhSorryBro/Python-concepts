# 8.15. Printing models.
# Place the functions from the print_models.py program in a separate file called print_models.py. At the top of the print_functions.py file, add an import statement and modify the file so that it uses the imported functions.
print("===")
import printing_functions

unprinted_designs = ['phone case', 'robot pendant', 'triangle']
completed_models = []

printing_functions.print_models(unprinted_designs, completed_models)
printing_functions.show_completed_models(completed_models)

# 8.16. Import statements.
# Use the function created by yourself — one function — and move it to a separate file. Import that function into the main program, and then call all the listed functions in the following ways:
# import module_name
# from module_name import function_name
# from module_name import function_name as fn
# import module_name as mn
# from module_name import *
print("===")

import make_sandwich_file
make_sandwich_file.make_sandwich('onion')
from make_sandwich_file import make_sandwich
make_sandwich('onion')
from make_sandwich_file import make_sandwich as ms
ms('onion')
import make_sandwich_file as msf
msf.make_sandwich('onion')
from make_sandwich_file import *
make_sandwich('oniononono')
# 8.17. Styling functions.
# Choose any three programs you created in this chapter and make sure they follow the naming conventions discussed in this chapter.
print("===")

def make_sandwich(*items):
    print(f"Preparing sandwich with {items}")

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
