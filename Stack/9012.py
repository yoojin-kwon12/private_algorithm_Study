# 9012번

"""
# 시작 체크 리스트
1. 1시간이 지났으나 발상 불가 또는 아예 다른 길
2. 코드 50% 정도 완성 0
3. 1시간 보다 더 걸려서 코드 완성.
4. 코드는 다 돌아가는데 효율성에서 걸림.
5. 코드완성

# 완료 후 체크 리스트
1. 아예 모르겠음
2. 중간 정도 이해함.
3. 완벽히 이해함. 0
"""

# 뭔가 규칙을 찾아서

"""
import sys

n = int(input())
inp = []

for i in range(n):
    # 이 방법으로 하니 마지막에 엔터가 인자로 저장이된다.
    # -> strip()으로 공백과 엔터 제거.
    ex = sys.stdin.readline().strip()
    for j in ex:
        print('---------------------------------')
        print(j)
        if j == '(':
            inp.append(j)
            print('inp' + str(inp))
        else:
            if len(inp) == 0:
                inp.append(j)
            else:
                if inp[-1] == '(':
                    inp.pop()
                    print('inp' + str(inp))
    if len(inp) == 0:
        print('YES')
    else:
        print('NO')

"""
# 이렇게 했는데 list index out of range가 났다. -> 조건을 잘 못걸었다.
# 이유는 알 수 없지만 같은 입력을 했음에도 결과가 다르게 나오는 경우가 여러번 생겼다.
# 그래서 다른 풀이방법을 찾아보았다.
# 풀이방법을 봐도 나랑 비슷하길래 뭐지...생각했다.
# 보니 inp 배열의 선언 위치였다.
# inp 배열을 입력받을때마다 초기화 시켜야되는데 그렇지 못하고 있으니 할때마다 값이 달랐던 것이다.

import sys

n = int(input())

for i in range(n):
    # 이 방법으로 하니 마지막에 엔터가 인자로 저장이된다.
    # -> strip()으로 공백과 엔터 제거.
    ex = sys.stdin.readline().strip()
    inp = []
    for j in ex:
        # print('---------------------------------')
        # print(j)
        if j == '(':
            inp.append(j)
            # print('inp' + str(inp))
        elif j == ")":
            if len(inp) != 0 and inp[-1] == '(':
                inp.pop()
            else:
                inp.append(j)
                # print('inp' + str(inp))
    if len(inp) == 0:
        print('YES')
    else:
        print('NO')

