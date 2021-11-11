def search_second_element():
    global arr, n
    l = 0
    r = arr[0]
    while (r - l > (0.01 / (n + 3))):
        arr[1] = (l + r) / 2
        flag = True
        for i in range(2, n):
            arr[i]  = 2 * arr[i - 1] - arr[i - 2] + 2
            if arr[i] < 0:
                flag = False
                break
        if flag:
            r = arr[1]
        else:
            l = arr[1]
    return arr[n - 1]


entry = open('garland.in', 'r').readlines()
out = open('garland.out', 'w')
n, a = [float(i) for i in entry[0].split()]
n = int(n)
arr = [float(i) for i in range(int(n))]
arr[0] = a
x = search_second_element()
x = str(x)
if len(x.split('.')[1]) > 2:
    x = x.split('.')[0] + '.' + x.split('.')[1][0:2]
out.write(x)
out.close()