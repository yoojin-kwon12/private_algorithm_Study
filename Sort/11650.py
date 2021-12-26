# 11650번

"""
# 시작 체크 리스트
1. 1시간이 지났으나 발상 불가 또는 아예 다른 길
2. 코드 50% 정도 완성
3. 1시간 보다 더 걸려서 코드 완성.
4. 코드는 다 돌아가는데 효율성에서 걸림. 0
5. 코드완성

# 완료 후 체크 리스트
1. 아예 모르겠음
2. 중간 정도 이해함.
3. 완벽히 이해함.
"""

# 시간 제한도 1초이고 최대 개수가 100,000이면 sort를 썼다간 무조건 시간초과가 날것 같았다.
# 하나씩 배열에 넣고 들어올때마다 비교를 하면 안될까...?

# 어떻게 어떻게 했는데...start가 여러번 들어가는 상황이 계속 발생한다.
# 왠지 이중 for문에서 안쪽 for문이 문제인듯한데...

"""
n = int(input())
result = [[0, 0]] # [[1,-1],[1,1],[3,4]]
answer = [[0, 0]]

for i in range(n):
    start = list(map(int, input().split())) # [2,2]
    if i == 0:
        result.append(start)
    print('start : ' + str(start))
    for j in range(i+1):
        if result[j][0] > start[0]:
            result.insert(j,start)
        elif result[j][0] == start[0]:
            if result[j][1] < start[1]:
                result.insert(j+1, start)
            else:
                result.insert(j,start)
        print('result : ' + str(result))

print(result)

"""

# 소요시간 1시간이 넘어서.. 풀이를 조금찾아보니...
# 다들 그냥 sort를 썼다..시간초과가 나지 않는 구나 싶었다...
# sort의 시간복잡도는 O(nlogn)이었다.
# 파이썬의 정렬 알고리즘은 https://questionet.tistory.com/61 참고. 다시 보고 정리.

n = int(input())
result = []

for i in range(n):
    result.append(list(map(int, input().split())))

result.sort(key=lambda x: (x[0],x[1]))

for i in result:
    print(i[0], i[1])
