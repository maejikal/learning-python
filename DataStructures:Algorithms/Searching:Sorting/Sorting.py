#merge sort
def merge_sort(lst):
    if len(lst) <= 1:
        return lst 
    mid = len(lst) // 2
    sorted_left = merge_sort(lst[:mid])
    sorted_right = merge_sort(lst[mid:])
    return merge(sorted_left, sorted_right)

def merge(lst1, lst2):
    p1 = 0
    p2 = 0
    ans = []
    while (p1 < len(lst1)) and (p2 < len(lst2)):
        if lst1[p1] < lst2[p2]:
            ans.append(lst1[p1])
            p1 += 1
        else:
            ans.append(lst2[p2])
            p2 += 1
    ans.extend(lst1[p1:])
    ans.extend(lst2[p2:])
    
    return ans


#merge sort for more complicated lists
#example [("john","tan"),("peter","tan"), ("samuel","lim"), ("sally","choo"), ("maxi","lim")]
#sort the list in alphabetical order of surname. For people with the same surname, 
#sort by alphabetical order of given name.
def compare(item1, item2):
    if item1[1] < item2[1]:
        return True
    elif item1[1] > item2[1]:
        return False
    elif item1[1] == item2[1]:
        if item1[0] < item2[0]:
            return True
        else:
            return False

def merge_sort(lst):
    if len(lst) <= 1:
        return lst 
    mid = len(lst) // 2
    sorted_left = merge_sort(lst[:mid])
    sorted_right = merge_sort(lst[mid:])
    return merge(sorted_left, sorted_right)

def merge(lst1, lst2):
    p1 = 0
    p2 = 0
    ans = []
    while (p1 < len(lst1)) and (p2 < len(lst2)):
        if compare(lst1[p1],lst2[p2]):
            ans.append(lst1[p1])
            p1 += 1
        else:
            ans.append(lst2[p2])
            p2 += 1
    ans.extend(lst1[p1:])
    ans.extend(lst2[p2:])
    
    return ans


#typical quick sort for a list of integers
def quicksort(left, right,lst):
    if right > left:
        pivot = partition(left, right, lst)
        quicksort(left, pivot - 1, lst)
        quicksort(pivot + 1, right, lst)
        
def partition(left, right, lst):
    p1 = left
    p2 = left
    while p2 < right:
        if lst[p2] < lst[right]: #for more complicated lists, do "if compare(element, pivot) with above function"
            lst[p1], lst[p2] = lst[p2], lst[p1]
            p1 += 1
            p2 += 1
        else:
            p2 += 1
    lst[p1], lst[right] = lst[right], lst[p1]
    return p1

    
 #insertion sort
 def insertionsort(lst):
    for p1 in range(1, len(lst)): #p1 is the item we're currently looking at. the list is sorted up to p1 (exclusive)
        p2 = p1 - 1
        while p2 >= 0 and lst[p1] < lst[p2]: #for more complicated lists, do "if compare(lst[p1], lst[p2])"
            lst[p1], lst[p2] = lst[p2], lst[p1]
            p1 -= 1
            p2 -= 1



#bubble sort
def bubblesort(lst):
    count = 0
    for p1 in range(0, len(lst)-1):#we need to do this n rounds
        print(count)
        swap = 0
        for p2 in range(0, len(lst)-p1-1):#compare p2 with p2+1. note last p1 items are already sorted
            if lst[p2] > lst[p2+1]: #for more complicated lists, do "if compare(lst[p1], lst[p2])"
                lst[p2], lst[p2+1] = lst[p2+1], lst[p2]
                swap = 1
        count += 1
        print(lst)
        if swap == 0: #terminate early if there are no swaps
            break