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
nums_list = []
nums_copy = []
new_nums = ""
temp_index = 0
max = ""

for digit in str(num):
    nums_list.append(str(digit))
    nums_copy.append(str(digit))

# Had to create a nums copy,
# Because since we .pop from the original list
# Its length shortens and the loop finishes earlier than it should
for index_i,i in enumerate(nums_copy):
    for index_j,j in enumerate(nums_list):
        if j > max:
            max = j
            temp_index = index_j
    new_nums += max
    nums_list.pop(temp_index)
    temp_index = 0
    max = ""

"""
Alternative way: 
return int("".join(sorted(str(num), reverse=True)))
"""    

print(int(new_nums))

