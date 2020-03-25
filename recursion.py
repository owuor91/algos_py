def list_sum(numbers):
    if len(numbers) == 0:
        return 0

    return numbers[0] + list_sum(numbers[1:])


def to_string(n, base):
    CHAR_FOR_INT = '0123456789abcdef'

    if n < base:
        return CHAR_FOR_INT[n]

    return to_string(n // base, base) + CHAR_FOR_INT[n % base]
