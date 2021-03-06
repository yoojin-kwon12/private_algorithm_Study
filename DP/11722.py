# 11722번
# 가장 긴 감소하는 부분 수열
# 딱 봐도 11053문제의 변형이었다.
# 그저 if문 부분만 바꾸면 될 것같다.
# 그치만 처음 푸는 것처럼 좀 더 <왜? 어떻게?>에 대해서 깊게 생각하면서 풀어보자.

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

# [10,30,10,20,20,10]에서 index 5 에 있는 10을 기준으로 생각해보자면
#              20 10
#           20    10
#     30          10
#     30    20    10
#     30       20 10
# 감소하는 부분의 케이스가 이렇게 있다. 그럼 이중에 가장 긴 (많은 값이 쓰인) 길이를 찾아야한다.
# 처음에는 뭔가 10을 기준으로 뒀을때 30이 10보다 크니까 추가하고....어쩌고 하는 방식을 생각해보았는데
# 알고리즘을 짤 수 없는 부분이라는 생각이 들었다. 패스.
# 그럼 처음부터 10을 기준으로 두지말고 30을 기준으로 시작해서 감소하는 숫자의 갯수를 더하는건 어떨까


n = int(input())

# [10,30,10,20,20,10]
dp = list(map(int, input().split()))

# rusult는 각 숫자를 기준으로 감소하는 숫자의 갯수의 초기값(자기자신이 1이므로)
result = [1] * n


# 기준이 되는 값의 앞의 값은 전부 비교해봐야하므로 이중 for문을 사용하자.
for i in range(1, n):
    for j in range(i):
        if dp[i] < dp[j]:
            result[i] = max(result[i], result[j] + 1)

print(max(result))