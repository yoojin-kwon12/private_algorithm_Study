# 1912번

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
3. 완벽히 이해함. 0
"""

# 그냥 이중 for문으로 돌면서 값을 다 저장하고 최댓값 뽑아내면 되지않나..?
# 물론 복잡도가...O(n^2)이겟지 -> 10,000,000,000 -> 습...쫌 빡센데 일단 해보자
# 음 역시 시간초과네

"""
n = int(input())
inp = list(map(int, input().split()))
result = []
for i in range(n):
    for j in range(i+1, n):
        result.append(sum(inp[i:j]))

print(max(result))
"""

# result 를 배열이 아니라 숫자로 선언해서...
# 새로운 더한 값이랑 기존의 result 값을 비교해서 더 큰값을 result에 다시 저장하면 되지않을까?
# 뭐 나름 하긴했는데 이것도 복잡도가 같네...흠

"""
n = int(input())
inp = list(map(int, input().split()))

result = 0
for i in range(n):
    for j in range(i+1, n):
        # sum(inp[a:b]) 사용
        # print("sum(inp[i:j]) : " + str(sum(inp[i:j])))
        # print("result : " + str(result))
        result = max(sum(inp[i:j]), result)
        # print("최종 result : " + str(result))

print(result)

"""
# 완전히 다른 문제라고 생각했는데 이전에 순열 문제와 같은 유형이구나..
# 기준을 0으로 잡지않고 1로 잡았으면 금방 생각해냈을수 있었을까?

n = int(input())
inp = list(map(int, input().split()))

for i in range(1,n):
    inp[i] = max(inp[i], inp[i-1] + inp[i])

print(max(inp))
















