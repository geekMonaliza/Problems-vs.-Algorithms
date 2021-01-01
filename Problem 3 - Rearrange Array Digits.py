def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """

    n = len(input_list)

    counts = [0 for e in range(10)]
    sorted_list = []
    for e in input_list:
        counts[e] = 1

    for i in range(0, 10):
        if counts[i] == 1:
            sorted_list.append(i)

    first_num = 0
    second_num = 0

    for i in range(n - 1, -1, -1):
        if i % 2 == 0:
            first_num = first_num * 10 + sorted_list[i]
        else:
            second_num = second_num * 10 + sorted_list[i]
    return [first_num, second_num]


def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")


test_function([[1, 2, 3, 4, 5], [542, 31]])
test_function([[4, 6, 2, 5, 9, 8], [964, 852]])
