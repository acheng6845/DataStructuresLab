import random
import timeit
import turtle

import sys


def sortselect(A, i, size=5, d=0):
   if len(A)<=size:
       A.sort()
       return A[i]
   start = 0
   medians = []
   while start < len(A):
       end = start + size
       if end > len(A):
           end = len(A)
       medians.append(A[start:end])
       start += size
   for a in medians:
       a.sort()
   medianslist = []
   for median in medians:
       if len(median) % 2 == 1:
           if len(median) != 1:
               medianslist.append(median[len(median)//2 + 1])
           else:
               medianslist.append(median[0])
       else:
           medianslist.append(median[len(median)//2])
   pivot=sortselect(medianslist,len(medianslist)//2)
   small, big = [], []
   for a in A:
       if a < pivot:
           small.append(a)
       elif a > pivot:
           big.append(a)
   if i < len(small):
       return sortselect(small, i, size, d+1)
   elif i == len(small):
       return pivot
   else:
       return sortselect(big, i-len(small)-1, size, d+1)

def timeFunction(f, n, repeat=1):
   return timeit.timeit(f.__name__ + '('+ str(n)+ ')', setup="from __main__ import " + f.__name__, number=repeat) / repeat


def printFunctionTimes(farray, array):
   for n in array:
       time1 = timeFunction(farray[0], n)
       time2 = timeFunction(farray[1], n)
       time3 = timeFunction(farray[2], n)
       print('n= ' + str(n) + ': fib1:  ' + str(time1) + ' fib2:  ' + str(time2) + ' fib3:  ' + str(time3))


def plotFunctionTimes(functions, colors, xrange, maxy, repeat=1):
   turtle.setworldcoordinates(xrange[0], 0, xrange[len(xrange) - 1], maxy)
   turtle.speed(0)
   for i in range(len(functions)):
       t = turtle.Turtle()
       t.pencolor(colors[i])
       for n in xrange:
           time = timeFunction(functions[i], n, repeat)
           t.goto(n, time)

def linearFunction(n):
   A = list(range(n))
   small = 0
   random.shuffle(A)
   for a in A:
       if a > small:
           small = a

def inplace(n):
    A = list(range(222))
    random.shuffle(A)
    inplaceselect(A, len(A) // 2, n)
def simple(n):
   A = list(range(222))
   random.shuffle(A)
   sortselect(A, len(A) // 2, n)
def isLinear():
   plotFunctionTimes(
       (simple, linearFunction),
       ("black", "red"),
       range(2, 200, 2), 0.001,
       repeat=10
   )
def testSize():
   plotFunctionTimes(
       (simple, linearFunction),
       ("black", "red"),
       range(2, 200, 2), 0.01,
       repeat=10
   )

def inplaceselect(A, k, size=5, start=0, end=-1, d=0):
    if end == -1:
       end = len(A)
    if end-start <= size:
       A[start:end] = sorted(A[start:end])
       #print(" "*d, "Short sequence: ", A, "from ", start, " to ", end, "- Returning ", A[k])
       return A[start+k]

    #print(" "*d,"selecting ", k, " in ", A, " from ", start, " to ", end)

    i = start
    while i < end:
        j = i + size
        if j > end:
            j = end
        A[i:j] = sorted(A[i:j])
        i = j

    #print(" "*d, "Sorted Groups: ", A)

    i = start + size // 2
    j = start + size - 1
    a = start
    while i < end:
        A[i], A[a] = A[a], A[i]
        if j != end - 1 and j + size >= end:
            #print(" "*d, "j: ", j)
            s = size // 2 + ((end - j - 1) // 2)
            if (end - j - 1) % 2 != 0:
                s += 1
            j = end - 1
        else:
            s = size
            j += s
        i += s
        a += 1

    range = (end-start) // size
    if end % size != 0:
        range += 1
    kth = range//2
    #print(" "*d, "Preparing for pivot ", A, "- Range: ", range)
    pivot = inplaceselect(A, kth, size, start, start+range, d+1)

    p = A.index(pivot)
    #print(" " * d, "Pivot: ", pivot, " at index - ", p)
    A[start], A[p] = A[p], A[start]
    i = start+1
    j = start+1
    smaller = 0

    while j < end:
        if A[j] <= pivot:
            A[j], A[i] = A[i], A[j]
            i += 1
            smaller += 1
        j += 1

    if k < smaller:
        return inplaceselect(A, k, size, start+1, start+smaller+1, d+1)
    elif k == smaller:
        return pivot
    else:
        return inplaceselect(A, k-smaller-1, size, start+smaller+1, end, d+1)

#isLinear()
#testSize()

# A = list(range(222))
# random.shuffle(A)
# print([inplaceselect(A,i) for i in range(222)])
#print(inplaceselect(A,30))

plotFunctionTimes(
       (simple, inplace),
       ("black", "red"),
       range(2, 200, 2), 0.001,
       repeat=10
)