def linear_search(array, element_to_find):
    for element in array:
        if element == element_to_find:
            return True
    return False