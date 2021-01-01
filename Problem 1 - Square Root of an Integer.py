def sqrt(number):
    if number < 0:
        return None

    square_root = 0
    temp = square_root

    while square_root <= (number // 2) + 1:
        square = square_root * square_root
        if square == number:
            return square_root

        if square > number:
            return temp
        temp = square_root
        square_root += 1


print("Pass" if (3 == sqrt(9)) else "Fail")
print("Pass" if (0 == sqrt(0)) else "Fail")
print("Pass" if (4 == sqrt(16)) else "Fail")
print("Pass" if (1 == sqrt(1)) else "Fail")
print("Pass" if (5 == sqrt(27)) else "Fail")
print("Pass" if (2 == sqrt(5)) else "Fail")
print("Pass" if (1 == sqrt(2)) else "Fail")
print("Pass" if (1 == sqrt(3)) else "Fail")
