class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.head = None

    def push(self, value):                 # 현재 [4] 밖에 없다면
        new_head = Node(value)             # [3] 을 만들고!
        new_head.next = self.head          # [3] -> [4] 로 만든다음에
        self.head = new_head               # 현재 head의 값을 [3] 으로 바꿔준다.
    
    def pop(self):
        if self.is_empty():                  # 만약 비어있다면 에러!
            return "Stack is empty!"
        delete_head = self.head              # 제거할 node 를 변수에 잡습니다.
        self.head = self.head.next           # 그리고 head 를 현재 head 의 다음 걸로 잡으면 됩니다.
        return delete_head                   # 그리고 제거할 node 반환
    
    def peek(self):
        if self.is_empty():
            return "Stack is empty!"

        return self.head.data
    
    def is_empty(self):
        return self.head is None