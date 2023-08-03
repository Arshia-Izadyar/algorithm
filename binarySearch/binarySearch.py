def binary_search(li, n):
    low = 0
    high = len(li) - 1
    li.sort()
    while low <= high:
        mid = (low + high) // 2
        guess = li[mid]
        if guess > n:
            high = mid -1 
        elif guess < n:
            low = mid + 1
        else:
            return mid
        

    return None

if __name__ == "__main__":
    print(binary_search([1, 2,3,4,5,6,10,7,8,9,0,11], 9)) 
    
        
        
