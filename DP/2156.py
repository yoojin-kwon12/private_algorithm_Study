# 2156번

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


# 다시보기...
# 대충의 규칙은 알겠으나 왜 이 규칙이 적용이 가능한지는 이해하지 못함.
# -> 다시 규칙을 찾아보니 wine[n]에서 answer[n]의 값이 될수 있는 경우의 수는
#    wine[n-1]에서 answer[n-1]의 값이 될수 있는 경우에서 같거나 추가된다는 사실을 알 수 있었다.
# => 문제를 접했을 때 가장 먼저 해야할 일은 규칙을 찾는것...
# 주어진 테스트 케이스를 예로 들어보면
# wine[4] = 9 이고 (wine[0]은 0으로 셋팅) 규칙에 따라
# index 2 + 3 / 1 + 2 + 4 / 1 + 3 + 4 이다.
# wine[5] = 8 이고
# index 2 + 3 + 5 (winde[4]의 경우 +5 ) / 1 + 2 + 4 + 5 (winde[4]의 경우 + 5) / 1 + 3 + 4 (winde[4]의 경우와 그대로) 이다.
# 이다. 그러므로 max(answer[j-1], answer[j-3] + wine[j-1] + wine[j], wine[j] + answer[j-2]) 식을 세울 수 있다.


n = int(input())
wine = [0]

for i in range(n):
    wine.append(int(input()))
answer = [0]
answer.append(wine[1]) # answer[1]

if n >1:
    answer.append(wine[1] + wine[2]) # answer[2]
for j in range(3, n+1):
    answer.append(max(answer[j-1], answer[j-3] + wine[j-1] + wine[j], wine[j] + answer[j-2]))
print(answer[n])


"""
a = []
for i in range(5):
    a.append(i)
print(a)
"""