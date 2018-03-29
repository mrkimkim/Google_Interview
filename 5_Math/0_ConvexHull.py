#-*- coding: utf-8 -*-
# 구글 면접 대비 0 - ConvexHull, Intersection, Orientation

"""
기본 출처 : https://www.geeksforgeeks.org/convex-hull-set-1-jarviss-algorithm-or-wrapping/

기하의 기본인 ConvexHull과 이것의 기반이 되는 Intersecion, Orientation
"""
import functools

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    def __init__(self, p, q):
        self.p = p
        self.q = q

# https://www.geeksforgeeks.org/orientation-3-ordered-points/
def orientation(p1, p2, p3):
    val = (p2.y - p1.y) * (p3.x - p2.x) - (p3.y - p2.y) * (p2.x - p1.x)
    if val == 0: return 0 # 평행
    return 1 if  val > 0 else 2 # 시계, 반시계

def onSegment(p1, p2, q1):
    if q1.x >= min(p1.x, p2.x) and q1.x <= max(p1.x, p2.x) \
        and q1.y >= min(p1.y, p2.y) and q1.y <= max(p1.y, p2.y):
        return True
    return False

# https://www.geeksforgeeks.org/check-if-two-given-line-segments-intersect/
def Intersect(L1, L2):
    o1 = orientation(L1.p, L1.q, L2.p)
    o2 = orientation(L1.p, L1.q, L2.q)
    o3 = orientation(L2.p, L2.q, L1.p)
    o4 = orientation(L2.p, L2.q, L1.q)
    print (o1, o2, o3, o4)
    if o1 != o2 and o3 != o4: return True

    if o1 == 0 and onSegment(L1.p, L1.q, L2.p): return True
    if o2 == 0 and onSegment(L1.p, L1.q, L2.q): return True
    if o3 == 0 and onSegment(L2.p, L2.q, L1.p): return True
    if o4 == 0 and onSegment(L2.p, L2.q, L1.q): return True
    return False

# O (N^2)의 ConvexHull
def ConvexHull(Points):
    Hull = []
    N = len(Points)
    # Find the Left Most
    l = 0
    for i in range(len(Points)):
        if Points[i].x < Points[l].x:
            l = i

    p = l;
    while True:
        Hull.append((Points[p].x, Points[p].y))
        # 현재 p에 대해 모든 점에 대해 반시계 방향에 놓인 점을 찾음
        # 최댓값 갱신과 같다고 생각하면 됨.
        q = (p + 1) % N
        for i in range(N):
            if orientation(Points[p], Points[i], Points[q]) == 2:
                q = i
        p = q

        if p == l: break

    return Hull

def Dist(p, q):
    return (p.x - q.x) ** 2 + (p.y - q.y) ** 2

def compare(q, r):
    global s
    if orientation(s, q, r) == 2:
        return False
    if orientation(s, q, r) == 0 and Dist(s, q) < Dist(s, r):
        return False
    return True

# O(N log N)의 ConvexHull
def ConvexHull2(P):
    global s

    l = 0
    N = len(P)
    # 최하단에 속하는 점들 중 제일 아래의 점을 택한다
    for i in range(1, N):
        if P[i].y < P[l].y or (P[i].y == P[l].y and P[i].x < P[l].x):
            l = i
    P[0], P[l] = P[l], P[0]
    s = P[0]

    # N - 1개의 점에 대해 P[0]에 대한 각도를 구한다.
    # Python 3.5의 커스텀 정렬함수 사용법
    sorted(P, key=functools.cmp_to_key(compare))

    # 같은 각도를 가지는 점 중 제일 작은 것만 남긴다.
    size = 1
    for i in range(1, N):
        while i < N - 1 and orientation(P[0], P[i], P[i+1]) == 0:
            i += 1
        P[size] = P[i]
        size += 1

    # 남은 점이 3개 이하라면 ConvexHull을 만들 수 없다.
    if size < 3: return -1

    # 스택을 만들어 초기의 3점을 집어넣는다
    Stack = [P[0], P[1], P[2]]
    Head = 2

    for i in range(3, size):
        while orientation(Stack[Head - 1], Stack[Head], P[i]) != 2:
            del Stack[Head]
            Head -= 1
        Stack.append(P[i])
        Head += 1
    return Stack

def PolygonArea(P):
    N = len(P)
    Sum = 0
    for i in range(N):
        Sum += (P[i].x * P[(i+1)%N].y - P[(i+1)%N].x * P[i].y)
    return 0.5 * abs(Sum)

p1, p2, p3, p4 = Point(1,1), Point(3,1), Point(2,2), Point(2,0)
L1, L2 = Line(p1, p2), Line(p3, p4)
isIntersect = Intersect(L1, L2)
print (ConvexHull([p1, p2, p3, p4]))
ConvexHull2([p1, p2, p3, p4])
print ("넓이 : ", PolygonArea(ConvexHull2([p1, p2, p3, p4])))