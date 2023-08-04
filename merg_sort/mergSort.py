def merg_sort(s):
    if len(s) < 2:
        return s
    mid = len(s) // 2
    left = merg_sort(s[:mid])
    right = merg_sort(s[mid:])
    return merg(left, right)


def merg(left, right):
    result = []
    i = 0
    j = 0
    print(left)
    while len(left) > i and len(right) > j:
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return "".join(result)

print(merg_sort("arshia"))
    