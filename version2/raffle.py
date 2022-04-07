"""Randomly pick customer and print customer info"""

import customers
import random

customers.get_customers_from_file('customers.txt')

def pick_a_winner():
    raffle_winner = random.choice(customers)
    print(customers)
    print(raffle_winner)
pick_a_winner()