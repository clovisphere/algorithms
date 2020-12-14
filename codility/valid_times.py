# Given 4 positive integers. Your task is to 
# return the total number of VALID TIME that 
# can be displayed on a digital clock (24 HOUR FORMAT)
# Return 0 if no VALID TIME can be displayed

import itertools

def validate(seq):
    # NOTE: valid time is between 00:00 and 23:59
    return (seq[0] * 10 + seq[1]) < 24 and (seq[2] * 10 + seq[3]) < 60

def f(*args): # ~> f(A, B, C, D)
    # sanity check -- none of the digit should be greater than 9:
    if [d for d in [*args] if d > 9]: return 0
    times = list(set(itertools.permutations([*args], 4))) # list of possible times
    return len([t for t in times if validate(t)])

if __name__ == '__main__':
    # let's "test" our solution -- use py.test next time, please:-)
    print(f'{f(1, 2, 3, 4)}')
    print(f'{f(0, 0, 0, 0)}')
    print(f'{f(3, 8, 11, 1)}')
    print(f'{f(0, 5, 7, 2)}')
