"""
Math 590
Project 1
Fall 2019

Partner 1:
Partner 2:
Date:
"""

"""
SelectionSort
"""
def SelectionSort(listToSort):
    for k in range(len(listToSort)):
        minimum = k
        for j in range(k, len(listToSort)):
            if listToSort[j] < listToSort[minimum]:
                minimum = j
        listToSort[minimum], listToSort[k] = listToSort[k], listToSort[minimum]

    return listToSort

"""
InsertionSort
"""
def InsertionSort(listToSort):
    for k in range(len(listToSort)-1):
        e = listToSort[k+1]
        for j in range(k+1):
            if listToSort[j] > e:
                listToSort[j+1:k+2] = listToSort[j:k+1]
                listToSort[j] = e
                break
    return listToSort

"""
BubbleSort
"""
def BubbleSort(listToSort):
    for i in range(len(listToSort)):
        for k in range(len(listToSort)-i-1):
            if listToSort[k] > listToSort[k+1]:
                listToSort[k],listToSort[k+1] = listToSort[k+1], listToSort[k]

    return listToSort

"""
MergeSort
"""
def MergeSort(listToSort):
    if len(listToSort) == 1:
        return listToSort.copy()
    if len(listToSort) == 2:
        return [min(listToSort), max(listToSort)]

    left = MergeSort(listToSort[ : len(listToSort)//2])
    right = MergeSort(listToSort[len(listToSort)//2 : ])
    i = 0
    j = 0
    for k in range(len(listToSort)):
        if i == len(left):
            listToSort[k:] = right[j:]
            break
        if j  == len(right):
            listToSort[k:] = left[i:]
            break
        if left[i] < right[j]:
            listToSort[k] = left[i]
            i+=1
        else:
            listToSort[k] = right[j]
            j+=1

    return listToSort

"""
QuickSort

Sort a list with the call QuickSort(listToSort),
or additionally specify i and j.
"""
def QuickSort(listToSort, i=0, j=None):
    # Set default value for j if None.
    def Partition(listToSort):
        pivot = i
        for k in range(i, j):
            if listToSort[k] < listToSort[pivot]:
                listToSort[pivot],listToSort[k] = \
                    listToSort[k],listToSort[pivot]
            
                listToSort[pivot+1],listToSort[k] = \
                    listToSort[k], listToSort[pivot+1]
                pivot += 1
        return pivot

    if j == None:
        j = len(listToSort)
    if j -i<=1:
        return listToSort
    pivot = Partition(listToSort)
    QuickSort (listToSort,i,pivot)
    QuickSort (listToSort,pivot+1, j)
    return listToSort

"""
Importing the testing code after function defs to ensure same references.
"""
from project1tests_updated import *

"""
Main function.
"""
if __name__ == "__main__":
    print('Testing Selection Sort')
    print()
    testingSuite(SelectionSort)
    print()
    print('Testing Insertion Sort')
    print()
    testingSuite(InsertionSort)
    print()
    print('Testing Bubble Sort')
    print()
    testingSuite(BubbleSort)
    print()
    print('Testing Merge Sort')
    print()
    testingSuite(MergeSort)
    print()
    print('Testing Quick Sort')
    print()
    testingSuite(QuickSort)
    print()
    print('DEFAULT measureTime')
    print()
    measureTime()
