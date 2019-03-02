
import random


def square_and_sum(x, y):
    x = x*x  # Square x
    return y + x  # Add y and return


def random_list(n):
    """ Returns a list of length n with random floats. Returns empty list for 
    negative n. """
    new_lst = []
    for _ in range(n):
        new_lst += random.randint(10, 100)
    return new_lst


def positive_num_to_string(n):
    n = str(n)
    if n <= 0:
        return n
    else:
        raise "Negative number!"
