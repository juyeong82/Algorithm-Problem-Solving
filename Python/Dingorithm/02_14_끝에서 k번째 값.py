# Q. 링크드 리스트의 끝에서 K번째 값을 반환하시오.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self, value):
        self.head = Node(value)
        
    def append(self, value):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(value)
        
    def get_kth_node_from_last(self, k):
        cur = self.head
        Node_length = 1
        while cur.next is not None:
            Node_length += 1
            cur = cur.next
        cur = self.head
        for _ in range(Node_length-k):
            cur = cur.next
            
    def get_kth_node_from_last(self, k):
        fast = self.head
        fast_cnt = 1
        slow_cnt = 0
        slow = self.head
        while fast.next is not None:
            if fast_cnt >= k:
                slow_cnt += 1
                slow = slow.next
            fast_cnt += 1
            fast = fast.next
            
        return slow
    
    def get_kth_node_from_last(self, k):
        fast = self.head
        slow = self.head
        
        for _ in range(k-1):
            if fast.next is None:
                raise IndexError("K가 리스트의 길이보다 커!")
            fast = fast.next
        
        while fast.next is not None:
            slow = slow.next
            fast = fast.next
            
        return slow
    
    
linked_list = LinkedList(6)
linked_list.append(7)
linked_list.append(8)

print(linked_list.get_kth_node_from_last(4).data)  # 7이 나와야 합니다!