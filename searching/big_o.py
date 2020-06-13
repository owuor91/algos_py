def find_min(list):
    min = list[0]
    for item in list:
        if item< min:
            min = item
    return min

def is_anagram2(s1, s2):
    if sorted(s1) == sorted(s2):
        return True
    return False