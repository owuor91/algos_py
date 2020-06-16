def sequential_search(item, list):
    position = 0
    while position < len(list):
        if list[position] == item:
            return True
        position += 1
    return False


def ordered_sequential_search(item, list):
    position = 0
    while position < len(list):
        if list[position] > item:
            return False

        if list[position] == item:
            return True

        position += 1
    return False


def binary_search(item, list):
    if not list:
        return False

    midpoint = len(list) // 2

    if list[midpoint] == item:
        return True

    if item < list[midpoint]:
        return binary_search(item, list[:midpoint])

    return binary_search(item, list[midpoint + 1:])
