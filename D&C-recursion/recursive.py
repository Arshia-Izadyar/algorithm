def fact(n):
    if n == 1:
        return n
    else:
        return n * fact(n-1)
    
    
def sum_(arr):
    if arr == []:
        return 0
    return arr[0] + sum_(arr[1:])

def sum__(arr):
    s = 0 
    for i in arr:
        s += i
    return s

def count_(arr):
    if arr == []:
        return 0
    else:
        return 1 + count_(arr[1:])
    
def count__(arr):
    c = 0
    for _ in range(len(arr)):
        c+= 1
    return c


def _sum(arr):
    if len(arr) == 0:
        return 0
    else:
        return arr[0] + _sum(arr[1:])
    
    
li = [1, 2, 3, 4, 5, 6 ,7, 8]
print(sum_(li))
print(sum__(li))
print(sum(li)) # sum
print(count_(li))
print(count__(li))