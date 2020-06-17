# [3,8,4,2,34,12,78,14]
def quick_sort(a_list):
    if len(a_list) <= 1:
        return a_list
    else:
        pivot = a_list.pop()

    lower_list = []
    higher_list = []
    for item in a_list:
        if item > pivot:
            higher_list.append(item)
        else:
            lower_list.append(item)

    return quick_sort(lower_list) + [pivot] + quick_sort(higher_list)

print(quick_sort([12, 54, 6, 32, 78, 4, 23, 1, 76, 8, 0, 43]))
