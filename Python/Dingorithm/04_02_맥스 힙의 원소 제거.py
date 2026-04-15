"""
      8      Level 0
    6   3    Level 1
   4 2 5     Level 2
   
 level 0/ 1   / 2
  0  / 1/ 2  3/ 4  5  6
[None, 8, 6, 3, 4, 2, 5]

1. 현재 인덱스 * 2 -> 왼쪽 자식의 인덱스
2. 현재 인덱스 * 2 + 1 -> 오른쪽 자식의 인덱스 1 * 2 + 1 =3
3. 현재 인덱스 // 2 -> 부모의 인덱스
4. 마지막 계층 시작인덱스 [len(heap)-1] * 2 - 1

"""

class MaxHeap:
    def __init__(self):
        self.items = [None]

    def insert(self, value):
        """
        # 원소 추가
        1. 맨 뒤에다가 원소를 넣는다.(현재 인덱스 = len(self.items)-1)
        2. 부모(현재 인덱스 // 2)와 비교해서 자기가 높으면 바꾼다
        3. 2의 과정을 부모가 더 크거나 루트 노드(인덱스 == 1)에 달했을때까지 반복한다.
        1 3 7 15
        """
        
        self.items.append(value)
        cur_index = len(self.items) - 1

        while cur_index > 1:  # cur_index 가 1이 되면 정상을 찍은거라 다른 것과 비교 안하셔도 됩니다!
            parent_index = cur_index // 2
            if self.items[parent_index] < self.items[cur_index]:
                self.items[parent_index], self.items[cur_index] = self.items[cur_index], self.items[parent_index]
                cur_index = parent_index
            else:
                break
                
    def delete(self):
        """
        # 원소 제거
        1. 루트 노드(인덱스 1)와 맨 끝에 있는 원소(len(self.items)-1)를 교체한다.
        2. 맨 뒤에 있는 원소를 (원래 루트 노드)를 삭제한다.
        3. 변경된 노드와 자식 노드들을 비교합니다. 두 자식 중 더 큰 자식과 비교해서 자신보다 자식이 더 크다면 자리를 바꿉니다.
        4. 자식 노드 둘 보다 부모 노드가 크거나 가장 바닥에 도달하지 않을 때까지 3. 과정을 반복합니다.
        5. 2에서 제거한 원래 루트 노드를 반환합니다.
        """
        cur_index = 1
        last_index = len(self.items) - 1
        
        self.items[cur_index], self.items[last_index] = self.items[last_index], self.items[cur_index]
        deleted_node = self.items.pop()
        
        child_idx_1 = 2
        child_idx_2 = 3
        
        # 자식노드가 없을때까지 반복
        while cur_index * 2 <= len(self.items) - 1:
            right_exists = child_idx_2 <= len(self.items) - 1
            if right_exists:
                if self.items[cur_index] < self.items[child_idx_1] or self.items[cur_index] < self.items[child_idx_2]:
                    if self.items[child_idx_1] > self.items[child_idx_2]:
                        self.items[cur_index], self.items[child_idx_1] = self.items[child_idx_1], self.items[cur_index]
                        cur_index = child_idx_1
                    else:
                        self.items[cur_index], self.items[child_idx_2] = self.items[child_idx_2], self.items[cur_index]
                        cur_index = child_idx_2
                    
                    child_idx_1 = cur_index * 2
                    child_idx_2 = cur_index * 2 + 1
                
            else: 
                break
        
        return deleted_node
    
    # 개선
    def delete(self):
        self.items[1], self.items[-1] = self.items[-1], self.items[1]
        prev_max = self.items.pop()
        cur_index = 1

        while cur_index * 2 <= len(self.items) - 1:
            child_idx_1 = cur_index * 2
            child_idx_2 = cur_index * 2 + 1
            right_exists = child_idx_2 <= len(self.items) - 1

            if right_exists and self.items[child_idx_2] > self.items[child_idx_1]:
                bigger_child = child_idx_2
            else:
                bigger_child = child_idx_1

            if self.items[cur_index] < self.items[bigger_child]:
                self.items[cur_index], self.items[bigger_child] = self.items[bigger_child], self.items[cur_index]
                cur_index = bigger_child
            else:
                break

        return prev_max
    
    # 정답
    def delete(self):
        self.items[1], self.items[-1] = self.items[-1], self.items[1]
        prev_max = self.items.pop()
        cur_index = 1

        while cur_index <= len(self.items) - 1:
            left_child_index = cur_index * 2
            right_child_index = cur_index * 2 + 1
            max_index = cur_index

            if left_child_index <= len(self.items) - 1 and self.items[left_child_index] > self.items[max_index]:
                max_index = left_child_index

            if right_child_index <= len(self.items) - 1 and self.items[right_child_index] > self.items[max_index]:
                max_index = right_child_index

            if max_index == cur_index:
                break

            self.items[cur_index], self.items[max_index] = self.items[max_index], self.items[cur_index]
            cur_index = max_index

        return prev_max
    



max_heap = MaxHeap()
max_heap.insert(8)
max_heap.insert(6)
max_heap.insert(7)
max_heap.insert(2)
max_heap.insert(5)
max_heap.insert(4)
print(max_heap.items)  # [None, 8, 6, 7, 2, 5, 4]
print(max_heap.delete())  # 8 을 반환해야 합니다!
print(max_heap.items)  # [None, 7, 6, 4, 2, 5]