def binary_search(arr, num, low=0, high=None):
    
    if high is None:
        high = len(arr) - 1
    if high < low:
        return None
    mid = (low + high) // 2
    guess = arr[mid]
    
    if guess > num: 
        return binary_search(arr, num, low, mid - 1)
    elif guess < num:
        return binary_search(arr, num, mid + 1, high)
    else:
        return mid
    


li = [1, 2, 3, 4, 5, 6, 7]

if __name__ == "__main__":
    print(binary_search(li, 3))