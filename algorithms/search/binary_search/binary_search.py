def binary_search(array, target_value):
    low_index = 0
    high_index = len(array) - 1
    midpoint = 0
 
    while low_index <= high_index:
        midpoint = (high_index + low_index) // 2
        if array[midpoint] < target_value:
            low_index = midpoint + 1

        elif array[midpoint] > target_value:
            high_index = midpoint - 1

        else:
            return midpoint
 
    return False