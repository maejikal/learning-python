def recur(lst, num):
    
    def helper(lst, l, r, num):
        if l <= r:
            mid = (l + r) // 2
            if lst[mid] == num:
                return mid
            elif lst[mid] > num:
                return helper(lst, l, mid - 1, num)
            else:
                return helper(lst, mid + 1, r, num)
        return -1
    
    return helper(lst, 0, len(lst) - 1, num)

def recur(lst, num):
    def helper(l, r, lst, num):
        if l <= r:
            half = (l+r) // 2
            if lst[half] == num:
                return half
            elif lst[half] > num:
                return helper(l, half-1, lst, num)
            else:
                return helper(half+1, r, lst, num)
        return -1
    return helper(0, len(lst)-1, lst, num)



def iter(lst, num):
    left = 0
    right = len(lst) - 1
    while left <= right:
        mid = (left +right) //2
        if lst[mid] == num:
            return mid
        elif lst[mid] > num:
            right = mid - 1
        else:
            left = mid + 1
    return -1

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(recur(lst, 3))

print(iter(lst, 8))


def iter(lst, num):
    left = 0
    right = len(lst) - 1
    while left <= right:
        mid = (left+right)//2
        if lst[mid] == num:
            return mid
        elif lst[mid] > num:
            right = mid-1
        else:
            left = mid+1
    return -1

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(recur(lst, 3))

print(iter(lst, 8))

