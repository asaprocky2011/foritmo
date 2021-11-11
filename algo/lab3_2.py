inn = open('sort.in', 'r').readlines()
out = open('sort.out', 'w')
n = int(inn[0])
arr = [int(i) for i in inn[1].split()]

def supp_heap_sort(arr, n, i):
    bigger = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left < n and arr[i] < arr[left]:
        bigger = left
    if right < n and arr[bigger] < arr[right]:
        bigger = right
    if bigger != i:
        arr[bigger], arr[i] = arr[i], arr[bigger]
        supp_heap_sort(arr, n, bigger)

def heap_sort(arr):
    n = len(arr)
    for i in range(n, -1, -1):
        supp_heap_sort(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        supp_heap_sort(arr, i, 0)

heap_sort(arr)
for i in range(n):
    if i == 0:
        out.write(str(arr[i]))
    else:
        out.write(' ' + str(arr[i]))
out.close()
