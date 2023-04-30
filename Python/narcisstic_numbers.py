# Your code must return true or false depending upon whether the given number is a Narcissistic number.

def narcissistic(value):
    sum = 0
    text = str(value)
    for digit in text:
        sum += pow(int(digit),len(text))
    if sum == value:
        return True
    return False 