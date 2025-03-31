'''convert to string task'''
class Node():
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

def stringify(node):
    outp = []
    temp = node
    while temp:
        outp.append(str(temp.data))
        temp = temp.next
    if temp is None:
        outp.append('None')
    return ' -> '.join(outp)



k = stringify(Node(0, Node(1, Node(2, Node(3)))))
print(k)
# stringify(None)
# stringify(Node(0, Node(1, Node(4, Node(9, Node(16))))))