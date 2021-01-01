def rotated_array_search(input_list, number, start_index, end_index ):
    """
    Find the index by searching in a rotated sorted array
    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    mid = (start_index + end_index)//2
    if start_index > end_index:
        return -1

    if input_list[mid] == number:
        return mid

    if input_list[start_index] < input_list[mid - 1]:
        if input_list[start_index] <= number <= input_list[mid - 1]:
            return rotated_array_search(input_list, number, start_index, mid - 1)
        else:
            return rotated_array_search(input_list, number, mid + 1, end_index)
    else:
        if input_list[mid + 1] <= number <= input_list[end_index]:
            return rotated_array_search(input_list, number, mid + 1, end_index)
        else:
            return rotated_array_search(input_list, number, start_index, mid - 1)


def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1


def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    output = rotated_array_search(input_list, number, 0, len(input_list) - 1)
    l_s = linear_search(input_list, number)
    if output == l_s:
        print("Pass")
    else:
        print("Fail")


test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])
test_function([[3, 4, 5, 6, 7, 1, 2], 7])
