def quickSort(arr):
    """Sort array using Bubble Sort"""
    elements = len(arr)
    if elements < 2:
        return arr
    current_position = 0
    for i in range(1, elements):
         if arr[i] <= arr[0]:
              current_position += 1
              temp = arr[i]
              arr[i] = arr[current_position]
              arr[current_position] = temp
    temp = arr[0]
    arr[0] = arr[current_position] 
    arr[current_position] = temp
    left = quickSort(arr[0:current_position])
    right = quickSort(arr[current_position+1:elements])
    arr = left + [arr[current_position]] + right
    return arr

def bubbleSort(array):
    """Sort array using Bubble Sort"""
    arr = list(array)
    n = len(arr)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def insertionSort(array):
    """"Sort array using Insertion Sort"""
    arr = list(array)
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >=0 and key < arr[j] :
                arr[j+1] = arr[j]
                j -= 1
        arr[j+1] = key
    return arr

def bogoSort(array):
    """Sort arr using Bogo Sort"""
    arr = list(array)
    from random import randint
    def is_sorted(a):
        n = len(a)
        for i in range(0, n-1):
            if (a[i] > a[i+1] ):
                return False
        return True
    def shuffle(a):
        n = len(a)
        for i in range (0,n):
            r = randint(0,n-1)
            a[i], a[r] = a[r], a[i]
    n = len(arr)
    while (is_sorted(arr)== False):
        shuffle(arr)
    return arr


from numpy import float64
from time import perf_counter as now
from json import loads
from sys import setrecursionlimit
setrecursionlimit(10**6)

with open("numbers.json","r") as d:
    data = loads(d.read())

print(len(data),type(data))

#with open("prenoms.txt","r") as d:
#    data = d.readlines()
#    for i,line in enumerate(data):
#        data[i] = line[-1]

#print(len(data),type(data))


quick_time_list = []
insertion_time_list = []
bubble_time_list = []

for i in range(2,1000):
    subdata = data[:i]
    print(i, end=" | ")
    
    quick_time_start = float64(now())
    quickSort(subdata)
    quick_time_end = float64(now())
    quick_execution_time = quick_time_end - quick_time_start
    quick_time_list.append(quick_execution_time)
    
    insertion_time_start = float64(now())
    insertionSort(subdata)
    insertion_time_end = float64(now())
    insertion_execution_time = insertion_time_end - insertion_time_start
    insertion_time_list.append(insertion_execution_time)
    
    bubble_time_start = float64(now())
    bubbleSort(subdata)
    bubble_time_end = float64(now())
    bubble_execution_time = bubble_time_end - bubble_time_start
    bubble_time_list.append(bubble_execution_time)


q, I, b = [], [], []

for i in range(2,1000,4):
    try:
        q.append(sum(quick_time_list[i:i+3])/4)
        I.append(sum(insertion_time_list[i:i+3])/4)
        b.append(sum(bubble_time_list[i:i+3])/4)
    except:
        break


import matplotlib.pyplot as plt
plt.scatter(range(2, 252), q,label="quick", marker='o',color="blue", s=1)
plt.scatter(range(2, 252), b, marker='o', label="bubble", color="red", s=1)
plt.scatter(range(2, 252), I, marker='o', label="insertion", color='black', s=1)
plt.xlabel("list length")
plt.ylabel("time")
plt.legend()
plt.show()


