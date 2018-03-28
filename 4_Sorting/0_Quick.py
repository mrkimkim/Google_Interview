#-*- coding: utf-8 -*-
# 구글 면접 대비 0 - Quicksort, QuickSearch

"""
기본 출처 : https://www.geeksforgeeks.org/kth-smallestlargest-element-unsorted-array/

O(n log n)의 수행시간을 가지는 QuickSort와 QuickSort를 이용한 k-th largest를 찾는 QuickSearch
"""

def partition(Arr, left, right, pivot):
    if left >= right: return
    i = left - 1
    for j in range(left, right):
        if Arr[j] <= pivot:
            i += 1
            Arr[i], Arr[j] = Arr[j], Arr[i]
    Arr[i + 1], Arr[right] = Arr[right], Arr[i + 1]
    return i + 1

def QuickSort(Arr, left, right):
    if left >= right: return
    pivot = Arr[int((left + right) / 2)]
    Arr[int((left + right) / 2)], Arr[right] = Arr[right], Arr[int((left + right) / 2)]
    mid = partition(Arr, left, right, pivot)
    QuickSort(Arr, left, mid - 1)
    QuickSort(Arr, mid + 1, right)
    return

def QuickSearch(Arr, left, right, k):
    if left > right: return
    if left == right and left == k: return Arr[left]

    pivot = Arr[int((left + right) / 2)]
    Arr[int((left + right) / 2)], Arr[right] = Arr[right], Arr[int((left + right) / 2)]

    mid = partition(Arr, left, right, pivot)
    if mid == k: return pivot
    elif mid > k: return QuickSearch(Arr, left, mid - 1, k)
    elif mid < k: return QuickSearch(Arr, mid + 1, right, k)



List = [1,3,10, 7, 4, 3, 5, 9, 2, 1, 6]
QuickSort(List, 0, len(List) - 1)
print (List)

List = [1,3,10, 7, 4, 3, 5, 9, 2, 1, 6]
k = 8
print (QuickSearch(List, 0, len(List) - 1, k - 1)) # index start from 0
print (List)