def calculate_average(numbers):
    n = 0
    for i in numbers:
        n += i
    return n / len(numbers)


def find_max(numbers):
    return max(numbers)


# numbers = [1, 2, 3, 11, 4, 5, 2]
# print(calculate_average(numbers))
# print(find_max(numbers))