from os import close


def bsort1(arr, l, r, n):
    if r - l == 1:
        if arr[l] == n:
            return l + 1
        elif arr[r] == n:
            return r + 1
        else:
            return -1
    mid = (l + r) // 2
    if n <= arr[mid]:
        return bsort1(arr, l, mid, n)
    else:
        return bsort1(arr, mid, r, n)

def bsort2(arr, l, r, n):
    if r - l == 1:
        if arr[r] == n:
            return r + 1
        elif arr[l] == n:
            return l + 1
        else:
            return -1
    mid = (l + r) // 2
    if n >= arr[mid]:
        return bsort2(arr, mid, r, n)
    else:
        return bsort2(arr, l, mid, n)

entry = open('binsearch.in', 'r').readlines()
out = open('binsearch.out', 'w')
n = int(entry[0])
arr = [int(i) for i in entry[1].split()]
m = int(entry[2])
arr2 = entry[3].split()
for i in arr2:
    out.write(str(bsort1(arr, 0, n - 1, int(i))) + ' ' + str(bsort2(arr, 0, n - 1, int(i))) + '\n')
out.close()


