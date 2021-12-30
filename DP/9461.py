# 9461번

"""
# 시작 체크 리스트
1. 1시간이 지났으나 발상 불가 또는 아예 다른 길
2. 코드 50% 정도 완성 0
3. 1시간 보다 더 걸려서 코드 완성.
4. 코드는 다 돌아가는데 효율성에서 걸림.
5. 코드완성

# 완료 후 체크 리스트
1. 아예 모르겠음
2. 중간 정도 이해함. 0
3. 완벽히 이해함.
"""
import sys

n = int(input())
result = []

for i in range(n):
    ex = int(sys.stdin.readline())
    dp = [0] * (ex + 1)
    dp[1] = 1
    dp[2] = 1
    for j in range(3, ex + 1):
        dp[j] = dp[j - 2] + dp[j - 3]
    result.append(dp[ex])

for i in result:
    print(i)

# 런타임에러가 났다...왜지...EORError 라고한다.
# sys.stdin.readline()로 바꾸니까 valueerror가 났다...뭐지..?
# 다른 풀이들을 보면 계속 n의 최대값이 100이니까 dp의 최대 크기가 100이라는데...
# 아닐수도 있지않나..?

