class Node:
    def __init__(self, data = None):
        self.data = data
        self.post = None

entry = open('postfix.in', 'r').readlines()
out = open('postfix.out', 'w')
first_element_index = -1
last_element_index = -1
arr = []
len_arr = 0
for j in entry[0].split():
    if j.isdigit():
        len_arr += 1
        element = Node(int(j))
        arr += [element]
        if last_element_index != -1:
            arr[-1].post = last_element_index
        last_element_index = len_arr - 1
    else:
        if j == "*":
            arr[last_element_index].data *= arr[arr[last_element_index].post].data
        elif j == "-":
            arr[last_element_index].data = arr[arr[last_element_index].post].data - arr[last_element_index].data
        elif j == "+":
            arr[last_element_index].data += arr[arr[last_element_index].post].data
        if arr[arr[last_element_index].post].post is not None:
            arr[last_element_index].post = arr[arr[last_element_index].post].post
        else:
            arr[last_element_index].post = None
out.write(str(arr[last_element_index].data))

out.close()  

