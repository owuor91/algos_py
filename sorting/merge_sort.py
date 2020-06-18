def merge_sort(list):
    if len(list) < 2:
        return list

    midpoint = len(list) // 2

    return merge(merge_sort(list[:midpoint]), merge_sort(list[midpoint:]))


def merge(left_list, right_list):
    if len(left_list) == 0:
        return right_list
    if len(right_list) == 0:
        return left_list

    result = []
    index_left = index_right = 0

    while len(result) <= len(left_list) + len(right_list):
        if left_list[index_left] <= right_list[index_right]:
            result.append(left_list[index_left])
            index_left += 1
        else:
            result.append(right_list[index_right])
            index_right += 1

        if index_left == len(left_list):
            result += (right_list)
            break
        if index_right == len(right_list):
            result += (left_list)
            break

    return result

# print(merge_sort([31,56,3,21,45,32,76,8756,43,23,5,6,788,8]))
