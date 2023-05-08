class Node ():
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList():
    def __init__(self):
      self.head = None

    def push(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while(current.next):
                current = current.next
            current.next = self.current = new_node

    def size(self):
        self.current = self.head
        num = 0
        while(self.current):
            self.current = self.current.next
            num += 1
        print(num)

    def top(self):
        current = self.head
        while (current.next):
            current = current.next
        print(current.value)

    def empty(self):
        if self.head is None:
            print(1)
        else:
            print(0)

    def pop(self):
        if self.head is not None:
          current = self.head
          while (current.next):
            current = current.next
          print(current.value)
          current = None
        else:
            print(-1)

num = int(input())

ll = LinkedList()

while(num>0):

  C = input()
  if " " in C:
    A, B = C.split()
    A = str(A)

  else:
    A = str(C)
    B = None

  if A == "push":
      ll.push(B)
  elif A == "pop":
      ll.pop()
  elif A == "empty":
      ll.empty()
  elif A == "top":
      ll.top()
  elif A == "size":
      ll.size()

  num -= 1
