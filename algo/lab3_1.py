inn = open('isheap.in', 'r').readlines()
out = open('isheap.out', 'w')
n = int(inn[0])
arr = [int(i) for i in inn[1].split()]
flag = True
for i in range(1, n + 1):
    if 2 * i <= n:
        if arr[i - 1] > arr[2 * i - 1]:
            flag = False
            break
    if 2 * i + 1 <= n:
        if arr[i - 1] > arr[2 * i]:
            flag = False
            break
if flag:
    out.write("YES")
else:
    out.write("NO")
out.close()
