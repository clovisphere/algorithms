"""Given a non-empty string s and a dictionary word_dict 
containing a list of non-empty words, determine if s can be segmented into 
a space-separated sequence of one or more dictionary words.

Note:
  - The same word in the dictionary may be reused multiple times in the segmentation. 
  - You may assume the dictionary does not contain duplicate words.

Example 1:
    Input : s = 'leetcode', word_dict = ['leet', 'code']
    Output: True

Example 2:
    Input : s = 'applepenapple', word_dict = ['apple', 'pen']
    Output: True

Example 3
    Input : s = 'catsanddog', word_dict = ['cats', 'dog', 'sand', 'cat']
    Output: False
"""

def word_break(s, word_dict):
    tt = [True] + [False] * len(s) # truth-table
    for index in range(1, len(tt)):
        for word in word_dict:
            if tt[index - len(word)] and s[:index].endswith(word):
                tt[index] = True
    return tt[-1]


if __name__ == '__main__':
    s, word_dict = 'cars', ['car', 'ca', 'rs']
    print(f'{s}, {word_dict}\nAnswer: {word_break(s, word_dict)}')
