# 예를 들어 아래와 같은 링크드 리스트를 입력받았다면,
# 각각 678, 354 이므로 두개의 총합
# 678 + 354 = 1032 를 반환해야 한다.


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


def get_linked_list_sum(linked_list_1, linked_list_2):
    cur1 = linked_list_1.head
    cur2 = linked_list_2.head
    number_of_list1 = 1
    number_of_list2 = 1
    
    while cur1.next is not None:
        cur1 = cur1.next
        number_of_list1 += 1
    
    while cur2.next is not None:
        cur2 = cur2.next
        number_of_list2 += 1
        
    cur1 = linked_list_1.head
    cur2 = linked_list_2.head
    number1 = 0
    number2 = 0
    for i in range(number_of_list1):
        ind1 = number_of_list1 - (i+1)
        number1 += cur1.data * 10**(ind1)  
        cur1 = cur1.next  
        
    for i in range(number_of_list2):
        ind2 = number_of_list2 - (i+1)
        number2 += cur2.data * 10**(ind2) 
        cur2 = cur2.next

    return number1 + number2

def get_single_linked_list_sum(linked_list):
    sum = 0
    cur = linked_list.head
    while cur is not None:
        sum = sum * 10 + cur.data
        cur = cur.next
        
    return sum
        

def get_linked_list_sum(linked_list_1, linked_list_2):
    sum_1 = get_single_linked_list_sum(linked_list_1)
    sum_2 = get_single_linked_list_sum(linked_list_2)
    
    return sum_1+sum_2

linked_list_1 = LinkedList(6)
linked_list_1.append(7)
linked_list_1.append(8)
linked_list_2 = LinkedList(3)
linked_list_2.append(5)
linked_list_2.append(4)

print(get_linked_list_sum(linked_list_1, linked_list_2))
