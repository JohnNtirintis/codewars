"""
The main idea is to count all the occurring characters in a string. If you have a string like aba, then the result should be {'a': 2, 'b': 1}.

What if the string is empty? Then the result should be empty object literal, {}.
"""

def count(string):
    charsDict = {}
    for letter in string:
        charsDict[letter] = charsDict.get(letter, 0) + 1
    return charsDict

#Alternative one-liner way:
def alt_count(string):
    return {i: string.count(i) for i in set(string)}