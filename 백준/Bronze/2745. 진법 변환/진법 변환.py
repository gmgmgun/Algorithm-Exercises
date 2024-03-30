n, b = input().split()


def convert_to_decimal(num, base):
    decimal = 0
    length = len(num)

    for i in range(length):
        char = num[i]
        value = 0

        if '0' <= char <= '9':
            value = int(char)
        elif 'A' <= char <= 'Z':
            value = ord(char) - ord('A') + 10

        weight = length - i - 1
        decimal += value * (int(base) ** weight)

    return decimal


print(convert_to_decimal(n, b))