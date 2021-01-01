def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """
    index = 0
    end_index = len(input_list) - 1
    zeros_index = 0

    while index <= end_index:
        if input_list[index] == 0:
            input_list[index] = input_list[zeros_index]
            input_list[zeros_index] = 0
            index += 1
            zeros_index += 1
        elif input_list[index] == 1:
            index += 1
        elif input_list[index] == 2:
            input_list[index] = input_list[end_index]
            input_list[end_index] = 2
            end_index -= 1
    return input_list

def test_function(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")


test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])