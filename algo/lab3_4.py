def down_heap_sort(arr, n, i):
    lower = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left < n and arr[left] < arr[i]:
        lower = left
    if right < n and arr[lower] > arr[right]:
        lower = right
    if lower != i:
        arr[i], arr[lower] = arr[lower], arr[i]
        down_heap_sort(arr, n, lower)

def up_heap_sort(arr, i):
    upper = (i - 1) // 2
    if i > 0 and arr[i][0] < arr[upper][0]:
        arr[i], arr[upper] = arr[upper], arr[i]
        up_heap_sort(arr, upper)

inn = open('priorityqueue.in', 'r').readlines()
out = open('priorityqueue.out', 'w')
arr = []
n = 0
flag_for_out = False
for i in inn:
    n += 1
    command_array = i.split()
    if len(command_array) == 2:
        command, element = command_array
        element = int(element)
        arr.append([element, n])
        up_heap_sort(arr, len(arr) - 1)
    elif len(command_array) == 1:
        if len(arr):
            arr[0], arr[-1] = arr[-1], arr[0]
            if flag_for_out:
                out.write('\n' + str(arr[-1][0]))
            else:
                out.write(str(arr[-1][0]))
                flag_for_out = True
            del arr[-1]
            down_heap_sort(arr, len(arr), 0)
        else:
            if flag_for_out:
                out.write('\n' + '*')
            else:
                out.write('*')
                flag_for_out = True
    else:
        x, y = [int(j) for j in command_array[1:]]
        for j in range(len(arr)):
            if arr[j][1] == x:
                arr[j][0] = y
                up_heap_sort(arr, j)
                break
out.close()
    
