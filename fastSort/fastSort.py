def fastSort(arr):
    if len(arr) < 2:
        return arr
    
    pivot = arr[0]
    lesser = [i for i in arr[1:] if i < arr[0]]
    grater = [i for i in arr[1:] if i > arr[0]]
    return fastSort(lesser) + [pivot] + fastSort(grater)


print(fastSort([31, 34 ,45, 23, 55, 12, 14, 98, 21]))