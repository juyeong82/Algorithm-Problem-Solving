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
        
    def get_node(self, index):
        cur = self.head
        for _ in range(index):
            cur = cur.next
        return cur
    
    def add_node(self, index, value):
        new_node = Node(value)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
        node = self.get_node(index-1)
        next_node = self.get_node(index)
        node.next = new_node
        new_node.next = next_node
    
    def delete_node(self, index):
        # [] -> [] -> []
        #    ------->
        # 0번째 노드는 다음 노드를 head로 만들어야 함.
        if index == 0:
            self.head = self.head.next
        # 지우려는 인덱스 이전 칸에서 다음칸으로 노드를 연결해주면 됨.
        node = self.get_node(index-1)
        node.next = node.next.next
        return 
    
linked_list = LinkedList(5) 
linked_list.append(12)
linked_list.append(34)

linked_list.add_node(1, 3)
linked_list.print_all()

linked_list.print_all()