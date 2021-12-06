# 11727번

"""
# 시작 체크 리스트
1. 1시간이 지났으나 발상 불가 또는 아예 다른 길 O
2. 코드 50% 정도 완성
3. 1시간 보다 더 걸려서 코드 완성.
4. 코드는 다 돌아가는 효율성에서 걸림.
5. 코드완성

# 완료 후 체크 리스트
1. 아예 모르겠음
2. 중간 정도 이해함.
3. 완벽히 이해함. O
"""

# n=4의 값을 틀림
# 피보나치 수열처럼 값의 규칙을 찾으려고 노력했으나 실패.

# (n=5) 일때 (n=4)의 타일링 하는 방법의 수에 (2*1) 타일을 붙이는 경우
#           (n=3)의 타일링 하는 방법의 수에 (2*2) 타일을 붙이는 경우
#           (n=3)의 타일링 하는 방법의 수에 (1*2) 타일을 붙이는 경우
# (n=3)의 타일링 하는 방법의 수에 (2*1) 타일을 붙이는 경우의 수가 들어가지 않는 이유는
# (n=4)의 타일링 하는 방법의 수와 중복되기 때문이다.


n = int(input())

dp = [0, 1, 3, 5]

for i in range(4, n+1):
    dp.append(dp[i-1] + (2 * dp[i-2]))
print(dp[n] % 10007)