def selection_sort(x_list):
    for i in range(0, len(x_list) - 1):
        minimum = i
        for j in range(i + 1, len(x_list)):
            if x_list[j] < x_list[minimum]:
                x_list[i], x_list[j] = x_list[j], x_list[i]
    return x_list


print(selection_sort([32, 43, 12, 8, 4, 32, 8, 1, 654, 23]))
