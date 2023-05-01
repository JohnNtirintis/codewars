"""
he goal of this exercise is to convert a string to a new string where each character in the new string is "(" if that character appears only once in the original string, or ")" if that character appears more than once in the original string. Ignore capitalization when determining if a character is a duplicate.

Examples
"din"      =>  "((("
"recede"   =>  "()()()"
"Success"  =>  ")())())"
"(( @"     =>  "))((" 
"""

def duplicate_encode(word):
    newWord = ""
    letterDict = {}

    for i in word:
        letterDict[i.lower()] = letterDict.get(i.lower(), 0) + 1
        
    for letter in word:
            if letterDict[letter.lower()] <= 1:
                newWord += "("
            elif letterDict[letter.lower()] > 1:
                newWord += ")"
    return newWord