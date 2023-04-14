# Implement the function which takes an array containing the names of people that like an item. 
# It must return the display text as shown in the examples:

"""
[]                                -->  "no one likes this"
["Peter"]                         -->  "Peter likes this"
["Jacob", "Alex"]                 -->  "Jacob and Alex like this"
["Max", "John", "Mark"]           -->  "Max, John and Mark like this"
["Alex", "Jacob", "Mark", "Max"]  -->  "Alex, Jacob and 2 others like this"

Note: For 4 or more names, the number in "and 2 others" simply increases.
"""

def likes(names):
    if not names:
        return "no one likes this"
    match len(names):
        case 1:
            return f"{names[0]} likes this"
        case 2:
            return f"{names[0]} and { names[1]} like this"
        case 3:
            return f"{names[0]}, {names[1]} and {names[2]} like this"
        case 4:
            return f"{names[0]}, {names[1]} and 2 others like this"
        case _:
            return f"{names[0]}, {names[1]} and {len(names) - 2} others like this"