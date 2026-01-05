
## all.py is the main file because it is the entry point from where the program execution starts.
from order import *

place_order("Alice", "ZARA", calculate_bill(2500, 1800, 3200))

##calculate_bill() runs first, returns the total, and that value is passed to place_order()

##The program calculates the total bill in one module, imports it into another module for order processing,-->
# and executes everything from a main file.

##output :
##Customer Name : Alice
#Brand         : ZARA
#Total Bill    : 7500