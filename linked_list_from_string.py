'''linked_list_from_string'''
class Node:
    def __init__(self, data, next=None):
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


def linked_list_from_string(s):
    if s == 'None':
        return None
    spl = s.split(' -> ')
    nodes = []
    for i in spl[:-1]:
        nodes.append(int(i))
    head = Node(nodes[0])
    temp = head
    for k in nodes[1:]:
        temp.next = Node(k)
        temp = temp.next
    return head

head = Node(0, Node(1, Node(4, Node(9, Node(16)))))
print(stringify(head))
print(linked_list_from_string('0 -> 1 -> 4 -> 9 -> 16 -> None'))
