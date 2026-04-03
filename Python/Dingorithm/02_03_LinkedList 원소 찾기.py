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
        
    def get_node(self, index):
        cur = self.head
        for _ in range(index):
            cur = cur.next
        return cur
    
    def get_node(self, index):
        cur = self.head
        cur_index = 0
        while cur_index != index:
            cur = cur.next
            cur_index += 1
        return cur

linked_list = LinkedList(5)
linked_list.append(12)
linked_list.append(34)
print(linked_list.get_node(0).data) # -> 0번 노드의 데이터: 5
print(linked_list.get_node(1).data) # -> 1번 노드의 데이터: 12
print(linked_list.get_node(2).data) # -> 2번 노드의 데이터: 34