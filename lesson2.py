#1. Binary search
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1

print("binary search:",binary_search([1, 3, 4, 6, 8], 6))




#2. merge sort
def merge(a, b):
    result = []
    i = 0
    j = 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1
    result.extend(a[i:])
    result.extend(b[j:])
    return result

def merge_sort(a):
    if len(a) <= 1:
        return a
    mid = len(a) // 2
    left = merge_sort(a[:mid])
    right = merge_sort(a[mid:])
    return merge(left, right)

print("merge_sort:",merge_sort([11, 32, 23, 44, 2]))

#3. Insertion Sort

def insertion_sort(arr):

    for i in range(len(arr)):
        key = arr[i]
        j = i-1

        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1

        arr[j+1] = key
    return arr

print("insertion_sort",insertion_sort([5, 2, 4, 1]))

#4.Quick Sort
def quick_sort_hoare(a):
    def partition(low, high):
        i = low
        j = high
        pivot = a[low]

        while True:
            while a[i] < pivot:
                i += 1

            while pivot < a[j]:
                j -= 1

            if i >= j:
                return j

            a[i], a[j] = a[j], a[i]
            i += 1
            j -= 1

    def _quick_sort(low, high):
        if low < high:
            p = partition(low, high)
            _quick_sort(low, p)
            _quick_sort(p+1, high)

    _quick_sort(0, len(a)-1)
    return a

print("quick_sort:", quick_sort_hoare([5, 2, 4, 1]))






