"""Given a non-empty string s and a dictionary word_dict 
containing a list of non-empty words, determine if s is valid 
based on all the dictionary words.

Example 1

Input : s = 'Practice makes pefect', word_dict = ['practice', 'makes', 'perfect']
Output: True

Example 2

Input : s = 'Practice makes perfect', word_dict = ['practice', 'perfect']
Output: False
"""


def valid_sentence(s, word_dict):
    if len(word_dict) != len(s): return False
    # there's probably a "cleaner" way to solve this 
    # but using sets doesn't hurt:-)
    A = set(s.lower().split(' '))
    B = set([e.lower() for e in word_dict])
    return True if len(A.difference(B)) == 0 else False


if __name__ == '__main__':
    string = 'Practice makes perfect'
    dictionary = ['practice', 'perfect']
    print(f'\'{string}\', {dictionary}\nAnswer: {valid_sentence(string, dictionary)}')
