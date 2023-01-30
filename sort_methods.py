def bubble_sort(strings):
    n = len(strings)
    for i in range(n):
        for j in range(0, n-i-1):
            if strings[j] > strings[j+1]:
                strings[j], strings[j+1] = strings[j+1], strings[j]
    return strings 

def insertion_sort(strings):
    n = len(strings)
    for i in range(1, n):
        key = strings[i]
        j = i-1
        while j >=0 and key < strings[j] :
                strings[j + 1] = strings[j]
                j -= 1
        strings[j + 1] = key
    return strings

def selection_sort(strings):
    n = len(strings)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if strings[j] < strings[min_idx]:
                min_idx = j
        strings[i], strings[min_idx] = strings[min_idx], strings[i]
    return strings

def shell_sort(strings):
    n = len(strings)
    gap = n//4
    while gap > 0:
        for i in range(gap,n):
            temp = strings[i]
            j = i
            while  j >= gap and strings[j-gap] >temp:
                strings[j] = strings[j-gap]
                j -= gap
            strings[j] = temp
        gap //= 2
    return strings

def merge_sort(strings):
    if len(strings) <= 1:
        return strings
    mid = len(strings)//2
    left = merge_sort(strings[:mid])
    right = merge_sort(strings[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result

def quick_sort(strings, low, high):
    if low < high:
        pivot = partition(strings, low, high)
        quick_sort(strings, low, pivot-1)
        quick_sort(strings, pivot+1, high)
    return strings

def partition(strings, low, high):
    pivot = strings[high]
    i = low - 1
    for j in range(low, high):
        if strings[j] <= pivot:
            i += 1
            strings[i], strings[j] = strings[j], strings[i]
    strings[i+1], strings[high] = strings[high], strings[i+1]
    return i + 1

def heap_sort(strings):
    n = len(strings)
    for i in range(n, -1, -1):
        heapify(strings, n, i)
    for i in range(n-1, 0, -1):
        strings[i], strings[0] = strings[0], strings[i]
        heapify(strings, i, 0)
    return strings

def heapify(strings, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and strings[i] < strings[l]:
        largest = l
    if r < n and strings[largest] < strings[r]:
        largest = r
    if largest != i:
        strings[i], strings[largest] = strings[largest], strings[i]
        heapify(strings, n, largest)