def Duplicate(x):
    _size = len(x) #aquires length of list
    duplicate = [] #new list
    for i in range(_size):
        k = i + 1
        #print(k), to see what k is doing
        for j in range(k, _size): #reads through list from point k to end of list (_size)
            if x[i] == x[j] and x[i] not in duplicate:
                duplicate.append(x[i]) #appends duplicate to list (duplicate)
    return duplicate

numbers = [1, 5, 7, 8, 10, 3, 5, 4, 10, 4, 7, 28, 54, 97, 28]

    
print(Duplicate(numbers))