"""
Math 590
Project 1
Fall 2019

Partner 1: Shu Yu Lee   sl603
Partner 2: Fang Feng   ff34
Date: 10/28/2019
"""

"""
SelectionSort

Separate the array into a sorted component and an unsorted component.
Iteratively search the unsorted component for the minimum element,
then place it at the end of the sorted component

Args:
  listToSort: A list to be sorted

Retruns:
  The original list object which is sorted
"""
def SelectionSort(listToSort):
    for k in range(len(listToSort)):
        minimum = k
        # Find the kth smallest element then swap it to the kth position
        for j in range(k, len(listToSort)):
            if listToSort[j] < listToSort[minimum]:
                minimum = j
        listToSort[minimum], listToSort[k] = listToSort[k], listToSort[minimum]

    return listToSort

"""
InsertionSort

Separate the array into a sorted component and an unsorted component.
Iteratively insert the element at k + 1 into the sorted component.

Args:
  listToSort: A list to be sorted

Retruns:
  The original list object which is sorted
"""
def InsertionSort(listToSort):
    for k in range(len(listToSort)-1):
        toBeInserted = listToSort[k+1]
        for j in range(k+1):
            if listToSort[j] > toBeInserted:
                # Move the whole slice between the original and the
                # destinated position of toBeInserted one to the right
                listToSort[j+1:k+2] = listToSort[j:k+1]
                listToSort[j] = toBeInserted
                break
    return listToSort

"""
BubbleSort

Iterate through the array. Compare every two adjacent elements.
If they are out of order, swap them. Repeat until no more swaps are made.

Args:
  listToSort: A list to be sorted

Retruns:
  The original list object which is sorted
"""
def BubbleSort(listToSort):
    for i in range(len(listToSort)):
        # Swap two adjacent elements if the former is larger than the latter
        # In the end, the kth largest element will be "bubbled" to
        # the kth position from the last
        for k in range(len(listToSort)-i-1):
            if listToSort[k] > listToSort[k+1]:
                listToSort[k],listToSort[k+1] = listToSort[k+1], listToSort[k]
    return listToSort

"""
MergeSort

Base Cases: If the array has 1 element, it is sorted.
            If the array has 2 elements, swap if needed and return.
Split the array into two halves. Recursively sort each half.
Then merge the already sorted halves.

Args:
  listToSort: A list to be sorted

Retruns:
  The original list object which is sorted
"""
def MergeSort(listToSort):
    if len(listToSort) == 1:
        return listToSort.copy()
    if len(listToSort) == 2:
        return [min(listToSort), max(listToSort)]

    # Split the list into two parts and sort them
    left = MergeSort(listToSort[ : len(listToSort)//2])
    right = MergeSort(listToSort[len(listToSort)//2 : ])

    # Merge left and right
    i = 0
    j = 0
    for k in range(len(listToSort)):
        # If i or j has reached the end of its corresponding list,
        # append the remaining part of the other list to listToSort
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

Base Cases: If the array has 1 element, it is sorted.
Partition the array based on the chosen pivot. Put everything smaller
than the pivot in front and everything larger than the pivot in back.
And recurse on each partition.

Sort a list with the call QuickSort(listToSort),
or additionally specify i and j.

Args:
  listToSort: A list to be sorted
  i: The starting index of the list slice to be sorted
  j: The ending index of the list slice to be sorted (excluded)

Retruns:
  The original list object which is sorted
"""
def QuickSort(listToSort, i=0, j=None):
    def Partition(listToSort):
        pivot = i
        for k in range(i, j):
            if listToSort[k] < listToSort[pivot]:
                # Move k to the left of pivot
                listToSort[pivot],listToSort[k] = \
                    listToSort[k],listToSort[pivot]
                # Move pivot to the correct position
                listToSort[pivot+1],listToSort[k] = \
                    listToSort[k], listToSort[pivot+1]
                # Update the pivot position
                pivot += 1
        return pivot

    # Set default value for j if None.
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
    measureTime(False)
