__author__ = 'Nikhil Ramesh'

def binary_search(input_array, left_index, right_index, value):
    mid_index = 0
    while (right_index - left_index) > 0:
        mid_index = left_index + int((right_index - left_index) / 2)
        if input_array[mid_index] < value:
            left_index = mid_index + 1
        else:
            right_index = mid_index - 1
    return left_index

def LIS(input_array):
    tail_array = [0 for _ in input_array]
    tail_array[0] = input_array[0]
    currentmax = 0
    for i in range(1,len(input_array)):
        item = input_array[i]

        # less than smallest item
        if item <= tail_array[0]:
            tail_array[0] = item
        elif item >= tail_array[currentmax]:
            currentmax += 1
            tail_array[currentmax] = item
        else:
            tail_array[binary_search(tail_array, 0, currentmax, item)] = item

    return currentmax + 1

val = LIS([2,4,3,15,10,14,6,7,8,4,10,5,8,9,11])
print(val)
