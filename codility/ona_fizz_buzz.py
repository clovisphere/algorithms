# A tweaked FizzBuzz problem,
# specific to Ona Kenya

import sys

def f(*args):
    array = [ int(el) for el in list(args)[0][1:] ]
    print(f'input: {array}')
    for el in array:
        _fail_for_all = True
        for e in range(1, el+1): 
            if e % 3 == 0 and e % 5 == 0:
                _fail_for_all = False
                print('OnaData', end=' ')
            elif e % 5 == 0:
                _fail_for_all = False
                print('Data', end=' ')
            elif e % 3 == 0:
                _fail_for_all = False
                print('Ona', end=' ')
        # if these conditions are not satisfied..
        print('N/A') if _fail_for_all else print()

if __name__ == '__main__':
    f(sys.argv)


