def insertion_sort(list):
    for i in range(1, len(list)):
        current_value, position = list[i], i

        while position > 0 and list[position - 1] > current_value:
            list[position], position = list[position - 1], position - 1
        list[position] = current_value
