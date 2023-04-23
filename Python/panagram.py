"""
A pangram is a sentence that contains every single letter of the alphabet at least once. For example, the sentence "The quick brown fox jumps over the lazy dog" is a pangram, because it uses the letters A-Z at least once (case is irrelevant).

Given a string, detect whether or not it is a pangram. Return True if it is, False if not. Ignore numbers and punctuation.
"""
def is_pangram(s):
    # Using a set because it doesnt accept duplicate values
    # We only have to iterate through the string and add the letters to the set
    # Then check if the length of the set is equal to the sum of the alphabet
    letter_set = set()
    for letter in s:
        # There is also punctuation in the string
        # So we have to check if the given char is a letter
        if letter.isalpha():
            letter_set.add(letter.lower())
    if len(letter_set) == 26:
        return True
    else:
        return False