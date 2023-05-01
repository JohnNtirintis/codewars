# You will be given an array of numbers. 
# You have to sort the odd numbers in ascending order while leaving the even numbers at their original positions.

def sort_array(source_array):
    for index in range(0, len(source_array)):
        for digit in range(index, len(source_array)):
            if source_array[index] % 2 != 0 and source_array[digit] % 2 != 0:
                if source_array[digit] < source_array[index]:
                    tmp = source_array[index]
                    source_array[index] = source_array[digit]
                    source_array[digit] = tmp
    return source_array
