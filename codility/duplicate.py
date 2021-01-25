import re

def find_duplicate(s):
    data = re.sub("[^a-zA-Z]", " ", s).lower().split(' ')
    result, _set = [], set()
    for d in data:
        if d and d in _set:
            result.append(d)
        _set.add(d)
    return result
        
if __name__ == "__main__":
    _str = "abc jghj Abc: glrg poll PoLL' tri ewqf Tri-"
    print(f'Given: {_str}')
    print(f'Duplicate: {find_duplicate(_str)}')
