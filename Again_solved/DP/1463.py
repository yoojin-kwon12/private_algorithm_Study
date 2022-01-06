
# 1463번

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
"""
import sys

n = int(sys.stdin.readline().strip())
inp = [0] * (n+1)
# inp = [0,0,1,1,2,3]

inp[2] = 1
inp[3] = 1
inp[4] = 2
inp[5] = 3
for i in range(6, n+1):
    if i % 2 == 0:
        inp[i] = inp[i // 2] + 1
        print(inp)
    elif i % 3 == 0:
        inp[i] = inp[i // 3] + 1
        print(inp)
    else:
        inp[i] = inp[i - 1] + 1
        print(inp)
print(inp[n])

"""

# 이와 같은 방법으로 했는데 n이 10일때의 답이 틀렸다.
# range에서 n으로 해서 index 오류가 났었다.
# list indices must be integers or slices, not float 라는 오류가 생겨서 찾아보니
#

# min을 사용해야되지 않을까..

# 만약 n이 2로만 나눠진다면?
# 만약 n이 3으로만 나눠진다면?
# 만약 n이 2,3 둘다 나눠진다면?
# 만약 n이 2,3 둘다 나눠지지 않는다면?

# 이방법을 사용햇더니 이전 방법보다 메모리 시간 모두 줄었다.

import sys

n = int(sys.stdin.readline().strip())
inp = [0] * 1000001
ex = 0
# inp = [0,0,1,1,2,3]

inp[2] = 1
inp[3] = 1
inp[4] = 2
inp[5] = 3
for i in range(6, n+1):

    # inp[i] = min(inp[i // 2] + 1, inp[i // 3] + 1, inp[i - 1] + 1)

    if i % 2 == 0 and i % 3 == 0:
        inp[i] = min(inp[i // 2] + 1, inp[i // 3] + 1, inp[i - 1] + 1)
        # print(inp)
    elif i % 2 == 0 and i % 3 != 0:
        inp[i] = min(inp[i // 2] + 1, inp[i - 1] + 1)
        # print(inp)
    elif i % 2 != 0 and i % 3 == 0:
        inp[i] = min(inp[i // 3] + 1, inp[i - 1] + 1)
    else:
        inp[i] = inp[i - 1] + 1

print(inp[n])