# 10825번

"""
# 시작 체크 리스트
1. 1시간이 지났으나 발상 불가 또는 아예 다른 길 0
2. 코드 50% 정도 완성
3. 1시간 보다 더 걸려서 코드 완성.
4. 코드는 다 돌아가는데 효율성에서 걸림.
5. 코드완성

# 완료 후 체크 리스트
1. 아예 모르겠음
2. 중간 정도 이해함.
3. 완벽히 이해함. 0
"""

# 이문제 역시 sort를 쓰는것은 비슷하나
# "sort의 key를 여러개를 설정할 줄 아는가" 와
# "아스키코드에서 대문자는 소문자보다 작으므로 사전순으로 앞에 온다"를 어떻게 표현할 것인가 를 물어보는 문제이다.

# 위의 두부분을 생각하지 못햇다.
# 오름차순일 때, -를 붙이는 것.
# 또한 파이썬에서 string을 오름차순으로 sort할 때, 원래 대문자부터 시작하기 때문에 고려할 필요가 없다.

n = int(input())
result = []

for i in range(n):
    result.append(input().split())
    result[i][1] = int(result[i][1])
    result[i][2] = int(result[i][2])
    result[i][3] = int(result[i][3])

# print(result)

result.sort(key= lambda x: ((-x[1]), x[2], (-x[3]),x[0]))

for i in result:
    print(i[0])