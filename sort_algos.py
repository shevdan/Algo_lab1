from copy import deepcopy
import math
import arr_gen
import time

def merge(left, right, sorted_lst, comparison):
    '''
    Help function to mergesort that merges two sorted arrays
    '''
    i, j, k = 0, 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            comparison += 1
            sorted_lst[k] = left[i]
            i += 1
        else:
            comparison += 1
            sorted_lst[k] = right[j]
            j += 1
        k += 1
        

    while i < len(left):
        comparison += 1     # comparison for loop condition
        sorted_lst[k] = left[i]
        i += 1
        k += 1
    
    while j < len(right):
        comparison += 1     # comparison for loop condition
        sorted_lst[k] = right[j]
        j += 1
        k += 1
    
    return sorted_lst, comparison


def merge_sort(arr: list, comparison=0):
    '''
    Divide and conquer sorting algorithm workin in O(n*log(n))
    '''
    if len(arr) > 1:
        mid = len(arr) // 2
        left, cmp1  = merge_sort(arr[:mid], comparison)
        right, cmp2 = merge_sort(arr[mid:], comparison)
        comparison = cmp1 + cmp2
        return merge(left, right, arr, comparison)
    return arr, 0

def insertion_sort(lst: list) -> list:
    '''
    Simple sorting algorithm working for O(n^2)
    Finds unsorted elements and puts them in it's
    place in sorted array
    '''
    comparison = 0
    for j in range(1, len(lst)): # iterate over each elm in array beginning from the 2nd
        key = lst[j]
        i = j - 1
        while i >= 0 and lst[i] > key:
            comparison += 1         # comparison for loop condition
            lst[i + 1] = lst[i] # shift every elm which is bigger than key and make space for key
            i -= 1
        lst[i + 1] = key
    return lst, comparison

def selection_sort(lst: list) -> list:
    '''
    Simple sorting algortithm working in O(n^2)
    on each iteration finds minimum elm in unsorted array
    and puts it in its sorted place at the sorted beginning
    '''
    comparison = 0
    for i in range(len(lst)):
        min_idx = i
        for j in range(i, len(lst)):
            if lst[j] < lst[min_idx]:
                comparison += 1
                min_idx = j
        lst[i], lst[min_idx] = lst[min_idx], lst[i]
    return lst, comparison

def shell_sort(lst: list) -> list:
    '''
    Optimized version of Insertion sort by sorting an array by gaps
    e.g. sorting every i-th position.
    '''
    gap = 1
    comparison = 0
    len_arr = len(lst)
    while gap< len_arr // 3:
        gap= 3*gap+ 1
    while gap>= 1:
        for i in range(gap, len_arr):
            j = i
            while j >= gap:
                if lst[j] < lst[j - gap]:
                    lst[j], lst[j - gap] = lst[j - gap], lst[j]
                    j -= gap
                    comparison += 1
                else:
                    comparison += 1
                    break
        gap //= 3
    return lst, comparison



if __name__ == "__main__":
    # arr = [6,2, 1,9, 3, 0, 5, 23 , 73, 123, 4]
    now = time.time()
    arr = arr_gen.rand_arr_gen(2**15)
    # print(merge_sort(deepcopy(arr))[1])
    # print(insertion_sort(deepcopy(arr))[1])
    # print(selection_sort(deepcopy(arr))[1])
    print(shell_sort(deepcopy(arr)))
    print(time.time() - now)


