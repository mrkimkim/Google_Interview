#-*- coding: utf-8 -*-
# 구글 면접 대비 2 - SegmentSeive

"""
기본 출처 : https://www.geeksforgeeks.org/euclidean-algorithms-basic-and-extended/
공간이 부족할 때 O(n)의 수행시간에 O(sqrt(n))의 공간으로 체와 유사하게 움직인다.
"""

def simpleSeive(n):
    isPrime = [True] * (n + 1)
    Prime = []
    for i in range(2, n + 1):
        if isPrime[i]:
            Prime.append(i)
            j = i * i
            while j <= n:
                isPrime[j] = False
                j += i
    return Prime

def SegmentSeive(n):
    limit = int(n ** 0.5)
    prime = simpleSeive(limit)
    for p in prime: print (p)
    low = limit
    high = low * 2

    while low < n:
        if high > n: high = n

        # 초기화
        marked = [True] * (high - low)

        # N보다 작은 모든 합성수는 반드시 sqrt(N)이하의 수를
        # 약수로 가진다.
        for i in range(len(prime)):
            s = (low // prime[i]) * prime[i]
            if s < low: s += prime[i]

            for j in range(s, high, prime[i]):
                marked[j - low] = False

        for i in range(low, high):
            if marked[i - low] == True:
                print (i)

        low += limit
        high += limit
    return

print (simpleSeive(7))
SegmentSeive(100)