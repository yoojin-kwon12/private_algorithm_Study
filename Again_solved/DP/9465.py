# 9465번

"""
# 시작 체크 리스트
1. 1시간이 지났으나 발상 불가 또는 아예 다른 길 0
2. 코드 50% 정도 완성
3. 1시간 보다 더 걸려서 코드 완성.
4. 코드는 다 돌아가는 효율성에서 걸림.
5. 코드완성

# 완료 후 체크 리스트
1. 아예 모르겠음
2. 중간 정도 이해함.
3. 완벽히 이해함.0
"""

import sys

n = int(sys.stdin.readline().strip())


for i in range(n):
    inp = []
    l = int(sys.stdin.readline().strip())
    for j in range(2):
        inp.append(list(map(int,sys.stdin.readline().split())))

    for h in range(1,l):
        if h == 1:
            inp[0][1] += inp[1][0]
            inp[1][1] += inp[0][0]
        else:
            inp[0][p] += max(inp[1][p-2],inp[1][p-1])
            inp[1][p] += max(inp[0][p-2],inp[0][p-1])
    print(max(inp[0][n - 1], inp[1][n - 1]))
# print(inp)