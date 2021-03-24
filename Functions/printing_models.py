#Importing module from printing_functions.py

import printing_functions as pf

unprinted_designs = ['phone case', 'robot pendant', 'toy']
completed_models = []

pf.print_models(unprinted_designs,completed_models)
pf.show_completed_models(completed_models)

