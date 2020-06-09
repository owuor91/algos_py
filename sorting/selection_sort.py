def selection_sort(list):
    for i in range(len(list)):
        min_position = i
        for j in range(i+1, len(list)):
            if list[min_position] > list[j]:
                min_position = j

        list[min_position], list[i] = list[i], list[min_position]
    return list