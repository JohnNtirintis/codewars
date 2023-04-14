"""
Your task is to make a function that can take any non-negative integer as an argument and 
return it with its digits in descending order. 
Essentially, rearrange the digits to create the highest possible number.

Examples:
Input: 42145 Output: 54421

Input: 145263 Output: 654321

Input: 123456789 Output: 987654321

"""

num = 42145
new_num = ""
counter = 0
max = 0
index = 0

s = str(num)

for index_i,i in enumerate(s):
    for index_j,j in enumerate(s):
        if str(j) > str(max) and index_j != index:
            max = j
            index = index_j
    new_num += str(max)
    max = 0

print(new_num)

# for index, item in enumerate(str(num)):
#     print(index, item)



