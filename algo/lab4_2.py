class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None

entry = open('queue.in', 'r').readlines()
out = open('queue.out', 'w')
n = int(entry[0])
arr = []
first_element_index = -1
last_element_index = -1
len_arr = 0
for i in range(1, n + 1):
    inn = entry[i].split()
    if len(inn) == 2:
        len_arr += 1
        element = Node(int(inn[1]))
        arr += [element]
        if first_element_index == -1:
            first_element_index = len_arr - 1
        else:
            arr[last_element_index].next = len_arr - 1
        last_element_index = len_arr - 1
    else:
        out.write(str(arr[first_element_index].data) + '\n')
        if arr[first_element_index].next is not None:
            first_element_index = arr[first_element_index].next
        else:
            first_element_index = -1
            last_element_index = -1
out.close()  



