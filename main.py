import pandas as pd
import matplotlib.pyplot as plt
import time as time
from sort_methods import *
import sys
sys.setrecursionlimit(1500)

file10k = open('nomes10k.txt', 'r',  encoding = 'utf-8')
namelist = file10k.readlines()

#descobre o tempo de execução do bubble sort para o arquivo
listbubble = namelist
timebubble = time.time()

listbubble = bubble_sort(listbubble)
print("tempo de execução do bubble sort: " + str(time.time() - timebubble))

#descobre o tempo de execução do insertion sort para o arquivo
listinsertion = namelist
timeinsertion = time.time()

listinsertion = insertion_sort(listinsertion)
print("tempo de execução do insertion sort: " + str(time.time() - timeinsertion))

#descobre o tempo de execução do selection sort para o arquivo
listselection = namelist
timeselection = time.time()

listselection = selection_sort(listselection)
print("tempo de execução do selection sort: " + str(time.time() - timeselection))

#descobre o tempo de execução do shell sort para o arquivo
listshell = namelist
timeshell = time.time()

listshell = shell_sort(listshell)
print("tempo de execução do shell sort: " + str(time.time() - timeshell))

#descobre o tempo de execução do merge sort para o arquivo
listmerge = namelist
timemerge = time.time()

listmerge = merge_sort(listmerge)
print("tempo de execução do merge sort: " + str(time.time() - timemerge))

#descobre o tempo de execução do quick sort para o arquivo
listquick = namelist
timequick = time.time()

listquick = quick_sort(listquick, 0, len(listquick) - 1)
print("tempo de execução do quick sort: " + str(time.time() - timequick))

#descobre o tempo de execução do heap sort para o arquivo
listheap = namelist
timeheap = time.time()

listheap = heap_sort(listheap)
print("tempo de execução do heap sort: " + str(time.time() - timeheap))

file10k.close()
