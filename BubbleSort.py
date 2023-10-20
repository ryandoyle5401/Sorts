from time import time
import random

class BubbleSort:
    def __init__(self):
        print("BubbleSort object created\n")


    def bub_sort(self, array):
        print("Normal Bubble Sort")
        print("Unsorted array", array)
        for i in range(len(array)-1):
            for j in range(0, len(array)-1-i):
                if array[j] > array[j+1]:
                    array[j], array[j+1] = array[j+1], array[j]
        print("Sorted Array",array)

    def adap_bub_sort(self, array):
        print("Adaptive Bubble Sort")
        swapped = False
        print("Unsorted array", array)
        for i in range(len(array)-1):
            for j in range(0, len(array)-1-i):
                if array[j] > array[j+1]:
                    array[j], array[j+1] = array[j+1], array[j]
                    swapped = True

            if not swapped: break
        print("Sorted array",array)

b = BubbleSort()
arr = [random.randint(1,100000) for i in range(5000)]
t0 = time()
b.bub_sort(arr)
t1 = time()
print("Normal Bubble Sort Time", t1-t0, "\n")

t2 = time()
arr2 = [1,3,2,4,5]
arr3 = [i for i in range(5000)]
b.adap_bub_sort(arr3)
t3 = time()
print("Adaptive Bubble Sort Time", t3-t2)
