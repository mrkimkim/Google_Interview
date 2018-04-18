#-*- coding: utf-8 -*-
# 구글 면접 대비 1 - 간단한 문제들

"""
기본 출처 : https://www.geeksforgeeks.org/swap-all-odd-and-even-bits/

[문] - 주어진 정수의 인접한 짝수와 홀수 비트를 서로 바꾸어라
정수가 32비트라고 가정하면 총 32개의 비트가 있다.

0xAAAAAAAA는 모든 짝수번째 비트가 1이고
0x55555555는 모든 홀수번째 비트가 1이다

이것을 각각 주어진 정수와 AND 연산하면 비트 분리가 가능하다.
짝수번째는 오른쪽 시프트, 홀수번째는 왼쪽 시프트를 하면
스왑이 가능하다.

https://www.geeksforgeeks.org/find-the-element-that-appears-once/
[문] - 주어진 배열에서 하나를 제외한 나머지 모든 숫자들은 3번씩
등장한다. 이 수를 구하여라

그 수의 비트는 반드시 3k + 1번 등장한다.

one과 two라는 변수를 0으로 초기화한다.
매 원소 Arr[i]마다

two |= (one & Arr[i])를 해준다.
ope = one ^ arr[i]를 해준다.

common_bit_mask = ~(ones & twos)이다.
즉, one과 two 모두에 포함되는 비트를 말한다.

one &= common_bit_mask
two &= commin_bit_mask

one은 1번만 등장하는 비트
two는 2번만 등장하는 비트를 저장한다.

two |= (one & Arr[i])를 통해 2번만 저장되는 비트를 얻는다.
해당 비트가 처음 등장할 때 one은 1이고 two는 0이다.
해당 비트가 두 번째 등장할 때 one은 0이고 two는 1이다.
해당 비트가 세 번째 등장할 때 one은 1이고 two는 1이다.
이 때 one과 two의 and를 통해 세 번째 등장하는 것만 묶어낼 수 있다.

이것의 반대를 one과 two에 and 연산해주면 켜진 비트에서 세 번째
등장하는 비트만을 제거할 수 있다.
"""