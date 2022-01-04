# 10828번

"""
# 시작 체크 리스트
1. 1시간이 지났으나 발상 불가 또는 아예 다른 길
2. 코드 50% 정도 완성
3. 1시간 보다 더 걸려서 코드 완성.
4. 코드는 다 돌아가는데 효율성에서 걸림.
5. 코드완성 0

# 완료 후 체크 리스트
1. 아예 모르겠음
2. 중간 정도 이해함.
3. 완벽히 이해함. 0
"""

import sys

n = int(input())
inp = []
stack = []

for i in range(n):
    inp = sys.stdin.readline().split()
    if inp[0] == 'push':
        stack.append(int(inp[1]))
    elif inp[0] == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    elif inp[0] == 'size':
        print(len(stack))
    elif inp[0] == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif inp[0] == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[len(stack)-1])
    else:
        print('명령어를 잘못입력하였습니다.')
