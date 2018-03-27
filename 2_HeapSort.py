#-*- coding: utf-8 -*-

# 구글 면접 대비 2 - MaxHeap 구현

"""
기본 출처 : https://www.geeksforgeeks.org/heap-data-structure/
최대 힙이란 완전 이진트리를 향하는 트리에서 자신의 좌우 자식 모두가
자기 자신보다 작은 조건이 모든 노드에 대해 만족하는 트리를 말한다.
따라서 루트는 그래프에서 최댓값을 가진다.
"""

class MaxHeap:
    # 초기화
    def __init__(self):
        self.Size = 0
        self.Heap = []

    # 원소의 삽입
    def insert(self, element):
        # 배열 마지막에 새 원소 추가
        self.Heap.append(element)

        if self.Size == 0:
            self.Size = 1
            return

        i = self.Size - 1
        # 조건이 만족하는 한 루트까지 간다
        while i > 0:
            # 부모보다 크면 교체한다
            parent = int((i - 1) / 2)
            if self.Heap[parent] < self.Heap[i]:
                self.Heap[parent], self.Heap[i] = self.Heap[i], self.Heap[parent]
                i = parent
            else: break
        self.Size += 1
        return

    # 원소의 제거
    def pop(self):
        if self.Size == 0: return None
        element, self.Heap[0] = self.Heap[0], self.Heap[self.Size - 1]
        del self.Heap[self.Size - 1]
        self.Size -= 1

        i = 0
        while i < self.Size:
            l = i * 2 + 1
            r = (i + 1) * 2

            if l < self.Size and self.Heap[l] > self.Heap[i]: l = l
            else: l = i

            if r < self.Size and self.Heap[r] > self.Heap[i]: r = r
            else: r = i

            # Max Child
            if self.Heap[l] > self.Heap[r]:
                child, value = l, self.Heap[l]
            else:
                child, value = r, self.Heap[r]

            if child == i: break
            if value > self.Heap[i]:
                self.Heap[i], self.Heap[child] = self.Heap[child], self.Heap[i]
                i = child
        return element

Heap = MaxHeap()
Heap.insert(3)
Heap.insert(5)
Heap.insert(1)
Heap.insert(3)
Heap.insert(3)
Heap.insert(5)
Heap.insert(1)
Heap.insert(3)
Heap.insert(3)
Heap.insert(5)
Heap.insert(1)
Heap.insert(3)
Heap.insert(4)

print (Heap.pop())
print (Heap.pop())
print (Heap.pop())
print (Heap.pop())
print (Heap.pop())