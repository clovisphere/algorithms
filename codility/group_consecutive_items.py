# Input : "aaaabbbcca"
# Output: [('a', 4), ('b', 3), ('c', 2), ('a', 1)]

import itertools

def f(seq):
    result, m = list(), dict()
    for k, v in enumerate(seq):
        if v in m:
            m[v] += 1
        else:
            m[v] = 1
        ### dictionary {'a': 1, 'b': 2} to list [('a', 1), ('b': 2)] ###
        if k == len(seq) - 1 or seq[k + 1] != v:
            result.append(list(m.items()))
            m.clear()
    return result if result else [(seq[0], 1)]

def f2(seq):
    return [(k, len(list(g))) for k, g in itertools.groupby(seq)]

if __name__ == '__main__':
    seq = 'aaaabbbcca'
    print(f'{seq}, {f(seq)}')
