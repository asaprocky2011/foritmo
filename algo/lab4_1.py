class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None
        self.post = None

entry = open('', 'r').readlines()
out = open('stack.out', 'w')
n = int(entry[0])
arr = []
last_element_index = -1
first_element_index = -1
len_arr = 0
for i in range(1, n + 1):
    inn = entry[i].split()
    if len(inn) == 2:
        len_arr += 1
        element = Node(int(inn[1]))
        arr += [element]
        if last_element_index == -1:
            last_element_index = len_arr - 1
        else:
            arr[-1].post = last_element_index
            arr[last_element_index].next = len_arr - 1
            last_element_index = len_arr - 1
    else:
        out.write(str(arr[last_element_index].data) + '\n')
        if arr[last_element_index].post is not None:
            arr[arr[last_element_index].post].next = None
            x = arr[last_element_index].post
            arr[last_element_index].post = None
            last_element_index = x
        else:
            last_element_index = -1
out.close()  



