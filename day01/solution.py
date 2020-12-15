#%% Part 1
def read_numbers(path):
    with open(path) as f:
        numbers = [int(number) for number in f.readlines()]
    return numbers


def find_sum_pair(numbers, target_sum):
    for number1 in numbers:
        # number1 = numbers.pop()
        for number2 in numbers:
            if number1 + number2 == target_sum:
                return (number1, number2)


numbers = read_numbers('input.txt')
number1, number2 = find_sum_pair(numbers=numbers, target_sum=2020)
print(number1 * number2)
# %% Part 2


def find_sum_triplet(numbers, target_sum):
    for number1 in numbers:
        # number1 = numbers.pop()
        for number2 in numbers:
            for number3 in numbers:
                if number1 + number2 + number3 == target_sum:
                    return (number1, number2, number3)


number1, number2, number3 = find_sum_triplet(numbers=numbers, target_sum=2020)

print(number1 * number2 * number3)
