from random import random
from math import ceil

def random_number():
    print('Your number is: ' + str(ceil(random()*100)))

random_number()