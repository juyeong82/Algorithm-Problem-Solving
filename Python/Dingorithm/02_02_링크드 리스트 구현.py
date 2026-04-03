class Node:
    def __init__(self, data):
        self.data = data
        self.next = None    
        # self.node or head.next 또한 node임

class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def append(self, value):
        cur = self.head             # head
        while cur.next is not None: #  [] -> []
            cur = cur.next          #     -> cur
        cur.next = Node(value)      #  self.head.next  = [value] 노드 생성 및 연결
    def print_all(self):
        cur = self.head
        while cur is not None:
            print(cur.data)
            cur = cur.next
        print("출력해보세요!")

linked_list = LinkedList(5)
print(linked_list.head.data)
linked_list.append(12)
print(linked_list.head.next.data)
linked_list.append(11)
print(linked_list.head.next.next.data)
linked_list.print_all()