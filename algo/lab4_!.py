class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None

entry = open('stack.in', 'r').readlines()
out = open('stack.out', 'w')
n = int(entry[0])
arr = []
last_element_index = -1
count_element = 0
for i in range(1, n + 1):
    inn = entry[i].split()
    if len(inn) == 2:
        element = Node(int(inn[1]))
        arr.append(element)
        count_element += 1
        if last_element_index != -1:
            arr[last_element_index].next = len(arr) - 1
        last_element_index = len(arr) - 1
    else:
        if count_element > 1:
            for j in range(len(arr)):
                if arr[j].next == last_element_index:
                    arr[j].next = None
                    break
        out.write(str(arr[last_element_index].data) + '\n')
        count_element -= 1
out.close()  



