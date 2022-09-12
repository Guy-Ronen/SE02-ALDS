def binary_search(array, target_value):
    low_index = 0
    high_index = len(array) - 1
    midpoint = 0
 
    while low_index <= high_index:
 
        midpoint = (high_index + low_index) // 2
 
        # If x is greater, ignore left half
        if array[midpoint] < target_value:
            low_index = midpoint + 1
 
        # If x is smaller, ignore right half
        elif array[midpoint] > target_value:
            high_index = midpoint - 1
 
        # means x is present at mid
        else:
            return midpoint
 
    # If we reach here, then the element was not present
    return False