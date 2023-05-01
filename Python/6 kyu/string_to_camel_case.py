"""
Complete the method/function so that it converts dash/underscore delimited words into camel casing. The first word within the output should be capitalized only if the original word was capitalized (known as Upper Camel Case, also often referred to as Pascal case). The next words should be always capitalized.

Examples:
"the-stealth-warrior" gets converted to "theStealthWarrior"

"The_Stealth_Warrior" gets converted to "TheStealthWarrior"

"The_Stealth-Warrior" gets converted to "TheStealthWarrior"
"""
def to_camel_case(text):
    answer = ""
    capitalLetter = ""
    for index, letter in enumerate(text):
        # It checks if the the given index is a letter and if its preceded by an underscore or hyphen
        # because if it does, then it must be capitalised so we dont want to add it now
        if letter.isalpha() and not (text[index - 1] == "_" or text[index - 1] == "-"):
            answer += letter
        # Ignores any underscores or hyphens
        elif letter == "_" or letter == "-":
            continue
        # if the given letter is preceded by an underscore or a hyphen
        # we will capitalise the given letter and add it to the answer string
        elif text[index - 1] == "_" or text[index - 1] == "-":
            capitalLetter = letter.upper()
            answer += capitalLetter
    return answer