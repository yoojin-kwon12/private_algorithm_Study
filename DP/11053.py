# 11053번
# LIS (Longest Increasing Subsequences) 라고 불리며 DP로 풀 수 있는 보편적인 문제 중 하나.
# 많이 참고한 블로그 : https://bitwise.tistory.com/215
# https://seohyun0120.tistory.com/entry/%EA%B0%80%EC%9E%A5-%EA%B8%B4-%EC%A6%9D%EA%B0%80%ED%95%98%EB%8A%94-%EB%B6%80%EB%B6%84-%EC%88%98%EC%97%B4LIS-%EC%99%84%EC%A0%84-%EC%A0%95%EB%B3%B5-%EB%B0%B1%EC%A4%80-%ED%8C%8C%EC%9D%B4%EC%8D%AC
# -> LIS 와 관련된 모든 문제들이 있다. 우선 2부터는 골드이므로...조금 실버문제에 익숙해지면 보자

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
3. 완벽히 이해함. 0
"""

# Dp를 써야하는지 어떻게 확신할것인가....
# -> 가장 긴 증가하는 부분이기때문에 배열의 인덱스가 커질수록 수가 플러스된다 -> DP일 수도 있다.
# DP를 기준으로 생각해보자.
#

"""
n = int(input())
inp = []
cnt = 0

inp = list(map(int, input().split()))

for i in range(0, len(inp)-1):
    cnt += 1
    if inp[i+1] <= inp[i]:
        inp[i+1] = inp[i]
        cnt -= 1

print(cnt+1)

"""
n = int(input())
inp = list(map(int, input().split()))

# 왜 배열의 초기값을 1로 했을까?
# -> 숫자 하나의 길이는 1이므로

result = [1] * n
for i in range(1,n):
    for j in range(i):
        if inp[j] < inp[i]:
            result[i] = max(result[i], result[j]+1)

print(max(result))




















