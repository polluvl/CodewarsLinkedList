class Node(object):
    """Node class for reference"""
    def __init__(self, data, next=None):
      """initializing a class Node"""
        self.data = data
        self.next = next

def get_nth(node, index):
  """
  a function to get a node in linkedlist for a give index
  """
    if not isinstance(index, int) or index < 0 or node == Node:
        raise ValueError
    counter = 0
    temp = node
    while temp:
        if index == counter:
            return temp
        temp = temp.next
        counter +=1
    raise ValueError
