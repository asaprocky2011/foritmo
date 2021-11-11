class Node:
    def __init__(self, data = None):
        self.data = data
        self.post = None

entry = open('brackets.in', 'r').readlines()
out = open('brackets.out', 'w')
for j in range(len(entry)):
    inn = entry[j]
    if inn[-1] == '\n':
        inn = inn[:len(inn) - 1]
    arr = []
    last_element_index = -1
    len_arr = 0
    for i in inn:
        flag = True
        if i == "[" or i == "(":
            len_arr += 1
            element = Node(i)
            arr += [element]
            if last_element_index != -1:
                arr[-1].post = last_element_index
            last_element_index = len_arr - 1
        else:
            if i == "]" and last_element_index != -1 and arr[last_element_index].data == "[":
                if arr[last_element_index].post is not None:
                    last_element_index = arr[last_element_index].post
                else:
                    last_element_index = -1
            elif i == ")" and last_element_index != -1 and arr[last_element_index].data == "(":
                if arr[last_element_index].post is not None:
                    last_element_index = arr[last_element_index].post
                else:
                    last_element_index = -1
            else:
                flag = False
                break
    if flag and last_element_index == -1:
        out.write("YES" + '\n')
    else:
        out.write("NO" + '\n')
out.close()  


