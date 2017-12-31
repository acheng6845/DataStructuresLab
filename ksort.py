def kSort(list, k, small, big):
    if small < big:
        if list[small] > k:
            if list[big] < k:
                list[small], list[big] = list[big], list[small]
                kSort(list, k, small+1, big - 1)
            else:
                kSort(list, k, small, big - 1)

        elif list[big] < k:
            kSort(list, k, small + 1, big)
        else:
            kSort(list, k, small + 1, big + 1)


def logTwo(n):
    n = n // 2
    if n >= 2:
        return 1+logTwo(n)
    else:
        return 1

A = [0]*5
for c in A:
    print(c)
    c=c+1

def rev(B):
    r = []
    while(len(B) > 0):
        r.append(B.pop())
    return r

print(rev([1,2,3]))
print(A[1:])

def flipArray(C):
    first = C[0]
    flipped = []
    C = C[1:]
    for i in range(len(first)):
        temp = [first[i]]
        for array in C:
            temp.append(array[i])
        flipped.append(temp)
    return flipped
print(flipArray([[1,2,3],[4,5,6],[7,8,9]]))

def f(n, i=0):
    if n>0:
        i=f(n-1,i)
        i=f(n-1,i)
    print(i)
    return i+1

def looptest(A):
    start = 0
    size = 4
    end = len(A)
    i = start + size // 2
    j = start + size - 1
    a = start
    while i < end:
        A[i], A[a] = A[a], A[i]
        if j != end - 1 and j + size >= end:
            s = size//2 + ((end - j - 1) // 2)
            if (end - j - 1) % 2 != 0:
                s += 1
            j = end - 1
        else:
            s = size
            j += s
        print(j)
        i += s
        a += 1


#f(2)

#print(len(12345))
A = [0,1,2,3,4,5,6,7,8,9]
looptest(A)
print(A)