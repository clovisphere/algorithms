# Given 4 digits, find the number of 
# possible time in a 24 hours format

import itertools

def validate(seq):
    # earliest ~ 00:00 | latest ~ 23:59
    return (seq[0] * 10 + seq[1]) < 24 and (seq[2] * 10 + seq[3]) < 60

def f(*args): # -> f(A, B, C, D) ~ we need four values
    times = list(set(itertools.permutations([*args], 4))) # list of possible times
    return len([t for t in times if validate(t)])


if __name__ == '__main__':
    # let's solution -- use py.test next time:-)
    print(f'{f(1, 2, 3, 4)}')
    print(f'{f(0, 0, 0, 0)}')
    print(f'{f(12, 45, 0, 1)}')
    print(f'{f(0, 5, 7, 2)}')
