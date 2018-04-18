#-*- coding: utf-8 -*-
# 구글 면접 대비 3 - Lucas Theorem

"""
기본 출처 : https://www.geeksforgeeks.org/compute-ncr-p-set-2-lucas-theorem/
nCr mod p를 O(p)의 공간내에서 구할 수 있게 해준다.
시간 복잡도는 O(p^2 * log n)이다.

nCr = PI(i = 0 to k) (n_i)C(r_i) (mod p)라는 정리다.

n과r이 모두 p보다 작은 경우에는 의미를 가지지 않는다.
"""

