# 11651

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

# 11650문제와 거의 동일한 문제여서 거의 그대로 풀었다.
# 처음에 결과값을 출력하는 방법을 range를 사용해서 print했다가 시간초과가 났다.
# range에서 시간초과가 나는지 아니면 str로 변형하는 부분이 시간초과가 나는지 확인해보니
# range였다.

# 다음에 시간초과가 날 경우, range도 고려해봐야겠다.

n = int(input())
result = []

for i in range(n):
    result.append(list(map(int,input().split())))

result.sort(key=lambda x: (x[1], x[0]))

for i in result:
    print(i[0],i[1])

"""
# 시간초과가 남.
for i in range(n):
    print(str(result[i][0]) + ' ' + str(result[i][1]))

# 시간초과가 나지않음.
for i in result:
    print(str(i[0]) + ' ' + str(i[1]))
    
# 시간초과 남.
for i in range(n):
    print(result[i][0], result[i][1])

"""