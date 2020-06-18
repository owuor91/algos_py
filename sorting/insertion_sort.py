def insertion_sort(list_x):
    sorted_list = []
    for item in list_x:
        sorted_list.append(item)
        item_index = len(sorted_list) - 1
        while item_index > 0 and sorted_list[item_index - 1] > sorted_list[item_index]:
            sorted_list[item_index - 1], sorted_list[item_index] = sorted_list[item_index], sorted_list[item_index - 1]
            item_index -= 1
    return sorted_list


print(insertion_sort([33, 2, 21, 45, 67, 2, 34, 87, 54, 3, 12, 6, 9]))
