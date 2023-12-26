# by HelderJFLima

# This is a simple script that generates a list of pseudo-random numbers.
#
# The user must inform the size of the list and the limits of the desired
# numbers.


import random
import sys

random.seed()                       # Initialize the random number generator

print('\n\n* Random numbers generator *\n')

minimum = int(input('Enter lower limit: '))

maximum = int(input('Enter upper limit: '))

quantity = int(input('Enter the desired quantity of numbers: '))

if minimum < 0:

    sys.exit('\nError: lower limit must be non-negative')

elif maximum <= 0:

    sys.exit('\nError: upper limit must be greater than zero')

elif quantity <= 0:

    sys.exit('\nError: quantity must be greater than zero')

print('\n')

for i in range(quantity):
    print(random.randint(minimum, maximum))
