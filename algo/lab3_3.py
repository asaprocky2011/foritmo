inn = open('radixsort.in', 'r').readlines()
out = open('radixsort.out', 'w')
n, m, k = [int(i) for i in inn[0].split()]
arr = []
for i in range(1, n + 1):
    if inn[i][-1] == '\n':
        arr.append(inn[i][:len(inn[i])-1])
    else:
        arr.append(inn[i])
count = 0
for i in range(m - 1, -1, -1):
    count += 1
    various = {'a': [], 'b': [], 'c': [], 'd': [], 'e': [], 'f': [], 'g': [], 'h': [], 'i': [], 'j': [],
           'k': [], 'l': [], 'm': [], 'n': [], 'o': [], 'p': [], 'q': [], 'r': [], 's': [], 't': [],
           'u': [], 'v': [], 'w': [], 'x': [], 'y': [], 'z': []}
    for j in range(n):
        various[arr[j][i]].append(arr[j])
    new_arr = []
    for j in various:
        new_arr += various[j]
    arr = []
    arr += new_arr
    if k == count:
        for j in range(n):
            if j == n - 1:
                out.write(str(arr[j]))
            else:
                out.write(str(arr[j]) + '\n')
        break
out.close()
