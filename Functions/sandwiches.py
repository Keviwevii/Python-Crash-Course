#Function using arbitrary arguments / importing a module

#Multiple ways to import modules / functions

import sandwich

from sandwich import make_sandwich

from sandwich import make_sandwich as ms

import sandwich as sw

from sandwich import *


sandwich.make_sandwich('potatoes', 'skittles')
sandwich.make_sandwich('chocolate', 'peanut butter')
sandwich.make_sandwich('idk', 'horseradish', 'condiments')