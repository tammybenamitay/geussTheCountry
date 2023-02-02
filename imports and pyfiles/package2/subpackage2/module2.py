from .module1 import adding_function #Relative import: Importing from a python file in the same location.
from ..constants import USEFUL_CONSTANT #Relative import: Importing from a python of one level up.

def add_to_constant(number):
	return adding_function(USEFUL_CONSTANT, number)