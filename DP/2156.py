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
2. 중간 정도 이해함. 0
3. 완벽히 이해함.
"""


# 다시보기...
# 대충의 규칙은 알겠으나 왜 이 규칙이 적용이 가능한지는 이해하지 못함.

n = int(input())
wine = [0]

for i in range(n):
    wine.append(int(input()))
answer = [0]
answer.append(wine[1]) # answer[1]

if n >1:
    answer.append(wine[1] + wine[2]) # answer[2]
for j in range(3, n+1):
    # print("2 : " + str(wine[j] + wine[j-2]))
    # print("3 : " + str(wine[j] + wine[j-1]))
    answer.append(max(answer[j-1], answer[j-3] + wine[j-1] + wine[j], wine[j] + answer[j-2]))
print(answer)


"""
a = []
for i in range(5):
    a.append(i)
print(a)
"""