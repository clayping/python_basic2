def calc_sum(numbers):
    total = 0
    for i in numbers:
        total += i
    return total


def calc_max(numbers):
    max = 0
    for j in numbers:
        if j > max:
            max = j
    return max


def calc_min(numbers):
    min = numbers[0]
    for k in range(1, len(numbers)):
        if numbers[k] < min:
            min = numbers[k]
    return min


def calc_avg(numbers):
    return calc_sum(numbers) / len(numbers)


def main():
    numbers = [int(tok) for tok in input("半角スペースをあけて複数の数値を入力: ").split()]

    print(calc_sum(numbers))
    print(calc_max(numbers))
    print(calc_min(numbers))
    print(calc_avg(numbers))


main()
