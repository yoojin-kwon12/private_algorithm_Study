# 10814번

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

# 11651번과 별반 다르지 않아보이지만 내 생각에 이 문제의 핵심은 21이 int이고 이름이 string이라는 것이다.
# 나이가 같으면 먼저 가입한 사람이 앞에 오는것은 이미 기초된 기준이므로 적용하지 않아도 될 것같다.
# pypy3으로 제출하니 더 빨리 결과가 나왔다. 16초 정도 걸렸다.
# python 3으로 제출하니 2분넘게 걸렸다.

n = int(input())
result = []

for i in range(n):
    result.append(input().split())
    result[i][0] = int(result[i][0])

# print(result)

result.sort(key=lambda x: x[0])

for i in result:
    print(i[0], i[1])

# 개인적으로 python과 pypy의 차이를 좀 알고 싶어졌다.
# tistory에 정리하겠다.

