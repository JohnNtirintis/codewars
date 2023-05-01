"""
Given a string of words, you need to find the highest scoring word.

Each letter of a word scores points according to its position in the alphabet: a = 1, b = 2, c = 3 etc.

For example, the score of abad is 8 (1 + 2 + 1 + 4).

You need to return the highest scoring word as a string.

If two words score the same, return the word that appears earliest in the original string.

All letters will be lowercase and all inputs will be valid.
"""
def high(x):
    score = 0
    word = ""
    wordsDict = {}
    for index, letter in enumerate(x):
        if not letter.isspace():
            word += letter
            score += ord(letter) - ord("a") + 1 
        if letter.isspace() or index + 1 == len(x):
            wordsDict[word] = score
            word = ""
            score = 0
    max_key = max(wordsDict, key=wordsDict.get)
    return max_key
    
