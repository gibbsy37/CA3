from time import sleep
import random


def roll():
    return random.choice([1, 2, 3, 4, 5, 6])


def bomb():
    """
    Raise an exception after a waiting a few seconds
    """
    wait = roll()
    for i in range(wait, 0, -1):
        print(i)
        sleep(1)
        if roll() == 1:
            print("Phew! The bomb didn’t explode")
            return
    message = random.choice(['jelly', 'gelignite', 'fruit', 'TNT', 'atom', 'bath']) + 'bomb'
    raise RuntimeError( message )


# Test it
try:
    print('Oops! Dropped the bomb')
    bomb()
except RuntimeError as e:
    print('The', e, 'exploded')