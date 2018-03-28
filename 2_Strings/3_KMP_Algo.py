#-*- coding: utf-8 -*-

# 구글 면접 대비 2 - KMP 알고리즘 구현

"""
기본 출처 : https://www.geeksforgeeks.org/searching-for-patterns-set-2-kmp-algorithm/
접미사 배열을 통해 패턴 매칭을 더욱 빠르게 수행할 수 있다.
"""

# 접미사 배열을 구한다
def getLPS(Str):
    lps = [0] * len(Str)
    lps[0] = 0
    Len = 0
    for i in range(1, len(Str)):
        while Str[i] != Str[Len] and Len != 0:
            Len = lps[Len - 1]

        if Str[i] == Str[Len]:
            Len, lps[i] = Len + 1, Len + 1
        else:
            Len, lps[i] = 0, 0
    return lps

# 매칭을 수행한다
def KMP(A, B):
    lps = getLPS(B)
    j = 0
    cnt = 0

    print ("LPS : ", lps)
    for i in range(len(A)):
        """
       A[i] != B[j]인 것은 A[i - 1]과 B[j - 1]까지는 일치했다는 것으로
       B[j - 1]의 최대 접미사 배열을 참조할 때 lps[j - 1]의 길이에 해당
       하는 B의 앞 부분은 A[i - 1]에서 뒤로 lps[j - 1]개의 문자와 일치한
       다는 것을 의미해 비교없이 일치함을 판별할 수 있기 때문이다.
       """
        while A[i] != B[j] and j != 0:
            j = lps[j - 1]

        if A[i] == B[j]:
            if j == len(B) - 1:
                print("Match from", i - j, "to", i)
                cnt += 1
                j = lps[j]
            else:
                j += 1

    return cnt



pattern_1 = input()
pattern_2 = input()
print (KMP(pattern_1, pattern_2))

