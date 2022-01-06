# 11727번

"""
# 시작 체크 리스트
1. 1시간이 지났으나 발상 불가 또는 아예 다른 길
2. 코드 50% 정도 완성
3. 1시간 보다 더 걸려서 코드 완성.
4. 코드는 다 돌아가는 효율성에서 걸림.
5. 코드완성 0

# 완료 후 체크 리스트
1. 아예 모르겠음
2. 중간 정도 이해함.
3. 완벽히 이해함. 0
"""

import sys

n = int(sys.stdin.readline().strip())
inp = [0] * 1001

inp[1] = 1
inp[2] = 3
inp[3] = 5

for i in range(4, n+1):
    inp[i] = inp[i-1] + (2 * inp[i-2])

print(inp[n] % 10007)