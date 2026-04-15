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

"""

class MaxHeap:
    def __init__(self):
        self.items = [None]

    def insert(self, value):
        """
        # 맥스 힙
        1. 맨 뒤에다가 원소를 넣는다.(현재 인덱스 = len(self.items)-1)
        2. 부모(현재 인덱스 // 2)와 비교해서 자기가 높으면 바꾼다
        3. 2의 과정을 부모가 더 크거나 루트 노드(인덱스 == 1)에 달했을때까지 반복한다.
        """
        
        # 구현해보세요!
        self.items.append(value)
        current_index = len(self.items)-1
        while current_index > 1:
            if self.items[current_index] > self.items[current_index // 2]:
                self.items[current_index], self.items[current_index // 2] = self.items[current_index // 2], self.items[current_index]
                current_index = current_index // 2
            else:
                break
                
        return

max_heap = MaxHeap()
max_heap.insert(3)
max_heap.insert(4)
max_heap.insert(2)
max_heap.insert(9)
print(max_heap.items)  # [None, 9, 4, 2, 3] 가 출력되어야 합니다!