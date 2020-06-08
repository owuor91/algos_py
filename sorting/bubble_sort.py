def bubble_sort(list):
    for pass_number in range(len(list)-1, 0, -1): #loop len(list) times starting from the end of the list
        for i in range(pass_number): #for each iteration compare and swap numbers upto excluding biggest/next biggest number which is already at the end of the list
            if list[i] > list[i+1]:
                list[i], list[i+1] = list[i+1], list[i] #simultaneous assignement