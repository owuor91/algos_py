def bubble_sort(m_list):
    sorted = False
    while not sorted:
        sorted = True  # breaking condition. if previous for loop was sorted this remains true & we can exit while loop
        for i in range(0, len(m_list) - 1):  # loop through every list item checking whether adjacent items are sorted
            if m_list[i] > m_list[i + 1]:
                sorted = False
                m_list[i], m_list[i + 1] = m_list[i + 1], m_list[i]  # swap unordered items in current position +1

    return m_list


print(bubble_sort([23, 14, 5, 12, 1, 8, 67, 432, 12, 65, 43, 6, 78, 409]))
