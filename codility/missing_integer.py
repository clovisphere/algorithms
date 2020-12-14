# Find the lowest missing integer N from a list/array A,
# N > 0 and A [-10000000...10000000]
# e.g [1, 2, 3] = 4
#     [3] = 1
#     [-1, -3] = 1

def missing_int(A):
    _set = set(A)
    for i in range(1, len(A)+2):
        if i not in _set: return i

if __name__ == '__main__':
    test_cases = [
        [3],
        [10, 10, 2, 2, 3, 3, 4],
        [-1, -3],
        [1, 3, 6, 4, 1, 2],
        [1, 2, 3]
    ]
    for tc in test_cases:
        print(f'for {tc}, the missing integer is: {missing_int(tc)}')

