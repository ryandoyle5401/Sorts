from time import time
import random

class BubbleSort:
    def __init__(self):
        print("BubbleSort obj created")\


    def bub_sort(self, array):
        print("Unsorted array", array)
        for i in range(len(array)-1):
            ####print(i)#was used for testing purposes
            for j in range(0, len(array)-1-i):
                ####print(i,j) #was used for testing purposes
                if array[j] > array[j+1]:
                    array[j], array[j+1] = array[j+1], array[j]
        print("Array after",array)

    def adap_bub_sort(self, array):
        swapped = False
        print("Unsorted array", array)
        for i in range(len(array)-1):
            ####print(i) #was used for testing purposes
            for j in range(0, len(array)-1-i):
                #print(i,j)
                if array[j] > array[j+1]:
                    array[j], array[j+1] = array[j+1], array[j]
                    swapped = True

            if not swapped: break
        print("Array after",array)

b = BubbleSort()
arr = [random.randint(1,100000) for i in range(5000)]
t0 = time()
b.bub_sort(arr)
t1 = time()
print("Time for normal Bubble Sort", t1-t0)

t2 = time()
arr2 = [1,3,2,4,5]
arr3 = [i for i in range(5000)]
print(arr3)
b.adap_bub_sort(arr3)
t3 = time()
print("Time for adaptive Bubble Sort", t3-t2)
