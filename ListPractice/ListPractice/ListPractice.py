class Empty:
    def __init__(self):
        self.IsEmpty = True
Empty = Empty()

class Node:
    def __init__(self, value, tail):
        self.IsEmpty = False
        self.Value = value
        self.Tail = tail
        
y = 0

l = Empty
m = Empty

cnt = int(input("how big of a list? "))
for i in range(0, cnt):
    a = input("What value? ")
    l = Node(a, l)
    
x = l

while not(x.IsEmpty):
    print(x.Value)
    m = Node(x.Value, m)
    x = x.Tail

y = m
print("-----------------------")

while not(y.IsEmpty):
    print(y.Value)
    y = y.Tail