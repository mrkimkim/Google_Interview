#-*- coding: utf-8 -*-
# 구글 면접 대비 0 - MergeBST

"""
기본 출처 : https://www.geeksforgeeks.org/merge-two-bsts-with-limited-extra-space/
두 개의 BST가 있을 때 제한된 공간 O(height1 + height2)에서 O(N + M)의 시간 내에
두 트리의 원소를 증가순으로 출력하여라
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def inorder(root):
    if root.left != None:
        inorder(root.left)
    print (root.data)
    if root.right != None:
        inorder(root.right)

s1 = [] # BST-1의 스택
s2 = [] # BST-2의 스택
Len1 = 0 # BST-1의 스택 크기
Len2 = 0 # BST-2의 스택 크기

BST1 = Node(8)
BST1.left = Node(2)
BST1.left.left = Node(1)
BST1.right = Node(10)

BST2 = Node(5)
BST2.left = Node(3)
BST2.left.left = Node(0)

cur1 = BST1
cur2 = BST2

# 모두가 0이 되면 탐색이 종료된다.
while cur1 != None or cur2 != None or Len1 != 0 or Len2 != 0:
    # 둘 중 하나가 완전히 탐색되지 않았을 때
    # 현재 노드의 왼쪽으로 가장 깊이 들어간다
    # 즉 현재 노드의 서브트리 중 가장 작은 원소
    # 를 찾아냄과 동시에 왼쪽 브랜치를 모두 저장한다.
    if cur1 != None or cur2 != None:
        while cur1 != None:
            s1.append(cur1)
            Len1 += 1
            cur1 = cur1.left

        while cur2 != None:
            s2.append(cur2)
            Len2 += 1
            cur2 = cur2.left

    # 왼쪽으로 더 들어갈 수도 없고, Stack도 비어있다면
    # 트리는 완전히 탐색된 것으로 다른 트리의 남은 영역만
    # inorder 탐색하면 된다.
    if Len1 == 0:
        while Len2 > 0:
            # pop stack2
            cur2 = s2[Len2 - 1]
            del s2[Len2 - 1]
            Len2 -= 1

            # 해당 노드의 subtree 중 자신과 오른쪽 것만 탐색하면 된다.
            cur2.left = None
            inorder(cur2)
            cur2 = None
        break

    if Len2 == 0:
        while Len1 > 0:
            # pop stack1
            cur1 = s1[Len1 - 1]
            del s1[Len1 - 1]
            Len1 -= 1

            cur1.left = None
            inorder(cur1)
            cur1 = None
        break

    # 현재 스택에는 각 노드에서 제일 작은 원소가 제일 위에 있다.
    # pop stack1
    cur1 = s1[Len1 - 1]
    del s1[Len1 - 1]
    Len1 -= 1

    # pop stack2
    cur2 = s2[Len2 - 1]
    del s2[Len2 - 1]
    Len2 -= 1

    # 현재 후보군 노드의 왼쪽은 이미 다 탐색됨.
    # 작은 노드를 출력하고 노드의 오른쪽을 살펴본다.
    # 큰 노드는 다시 스택으로 넣는다.
    if cur1.data < cur2.data:
        # 현재 노드를 출력하기 이전에 왼쪽은 이미 다 탐색되었다.
        # 따라서 현재 것을 출력하고 자신의 오른쪽 자식으로 넘어가면 된다.
        # Stack에는 자신의 부모가 저장되어 있으므로 오른쪽 자식의 탐색이
        # 모두 끝나고 나면 부모 노드로 넘어간다.
        print (cur1.data)
        cur1 = cur1.right

        # push stack2
        s2.append(cur2)
        Len2 += 1
        cur2 = None
    else:
        print (cur2.data)
        cur2 = cur2.right

        # push stack1
        s1.append(cur1)
        Len1 += 1
        cur1 = None

