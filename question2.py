#Given two sorted linked lists consisting of N and M nodes respectively. In which you have to merge two objects and return a single objects.
#code:
class Node:
    def __init__(self, key):
        self.key = key
        self.next = None        
 
""" # return a newnode
def newNode(key):
    return Node(key)  """
 
# driver code
#let us create two sorted linked lists to test the above
#function. Created lists shall be
#a: 5->10->15->40
#b: 2->3->20
a = Node(3)
a.next = Node(8)
a.next.next = Node(4)
a.next.next.next = Node(12)
 
b = Node(15)
b.next = Node(1)
b.next.next = Node(6)
b.next.next.next = Node(19)
 
v = []
while(a is not None):
    v.append(a.key)
    a = a.next
 
while(b is not None):
    v.append(b.key)
    b = b.next
 
v.sort()
result = Node(-1)
temp = result
for i in range(len(v)):
    result.next = Node(v[i])
    result = result.next
 
temp = temp.next
print("Resultant Merge Linked List is : ")
while(temp is not None):
    print(temp.key, end=" ")
    temp = temp.next