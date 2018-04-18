#-*- coding: utf-8 -*-
# 구글 면접 대비 0 - 최대 XOR 부분 배열

"""
기본 출처 : https://www.geeksforgeeks.org/find-the-maximum-subarray-xor-in-a-given-array/

임의의 정수 배열이 주어질 때 XOR 값이 최대가 되는 부분 배열을 찾아낸다.
여기서 Subarray는 원본 Array를 연속한 구간으로 자른 것만을 의미한다.

[Simple Solution] - 이중 루프

[O(n) Solution]
모든 정수들이 고정된 비트 수를 가진다면 Trie Data Structure를 사용한다.

1. 빈 트리를 생성한다. 트리의 모든 노드는 0과 1의 값을 갖는 자식을 가진다.

2. pre_xor = 0을 Trie에 삽입한다.
이 작업은 pre_xor이 고정된 비트 (INT 32)를 가지고 있다는 가정하에
비트별로 0과 1의 자식 노드를 택하거나 새로 만들어서 마지막 비트에
도달하면 pre_xor을 해당 노드의 value에 저장한다. 상위비트부터

3. result = -inf

4. 배열의 원소 arr[i]에 대해 다음의 작업을 수행

4-1. pre_xor = pre_xor ^ arr[i]을 노드에 삽입
pre_xor은 a[0] ~ a[i]까지의 xor을 담게 됨

4.2 arr[i]로 끝나는 Trie의 최대 xor 값을 요청

상위 비트부터 하위비트로 향하는 동안 pre_xor의 현재 비트와
다른 비트값을 가지는 노드가 있는지 확인하며 가능한 그 비트를
향하도록 한다.

4.3 4.2에서 얻어진 값이 result보다 크다면 업데이트
"""
import sys

INT_SIZE = 32
INT_MIN = -sys.maxsize
class Node:
    def __init__(self):
        self.value = 0
        self.Child = [None, None]
        self.endpoint = -1

def insert(pre_xor, endpoint):
    global root

    tmp = root
    for i in range(INT_SIZE, -1, -1):
        bit = bool(pre_xor & (1 << i))
        if tmp.Child[bit] == None:
            tmp.Child[bit] = Node()
        tmp = tmp.Child[bit]
    tmp.value = pre_xor
    tmp.endpoint = endpoint
    return

def query(pre_xor):
    global root
    tmp = root
    for i in range(INT_SIZE, -1, -1):
        bit = bool(pre_xor & (1 << i))
        if tmp.Child[1 - bit] != None:
            tmp = tmp.Child[1 - bit]
        elif tmp.Child[bit] != None:
            tmp = tmp.Child[bit]
    return pre_xor ^ tmp.value, tmp.endpoint

def Process(Arr):
    # 변수 초기화
    pre_xor = 0
    result = INT_MIN
    l, r = -1, -1

    # 작업 시작
    insert(0, -1)
    for i in range(len(Arr)):
        pre_xor ^= Arr[i]
        insert(pre_xor, i)

        t1, t2 = query(pre_xor)
        if result < t1:
            result = t1
            l, r = t2, i

    # 결과 리턴
    return result, l + 1, r

# Extra - 시작 지점과 끝 지점을 알 수 있을까? (해냄)

root = Node()
Arr = [8, 1, 2, 12, 7, 6, 31]
MaxXOR = Process(Arr)
print (MaxXOR)

