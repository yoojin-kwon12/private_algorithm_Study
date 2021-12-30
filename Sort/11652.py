# 11652번

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

"""
import sys

n = int(input())
min_result = [0] * (pow(2,62) + 1) # -2^62 ~ 0 -> 0 ~ -2^62
plus_result = [0] * (2**62 + 1) # 0 ~ 2^62

for i in range(n):
    ex = int(sys.stdin.readline())
    if ex < 0:
        min_result[-ex] += 1 # ex가 마이너스니까
    else:
        plus_result[ex] += 1


print(min_result)
print(plus_result)
"""

# 위의 방법으로 해서 오류가 없는지 테스트를 해보려고 실행했는데 MemoryError가 나왔다...
# 찾아보니 64비트 파이썬 에서 list의 퇴대크기는 1,152,921,504,606,846,975개라고 한다.
# 2 **62가 너무 큰 것같은데 그럼 어떻게 처리해야할까...
# 뭐 반으로 잘라서 2,305,843,009,213,693,952 인데 그래도 python list 최대크기보다 크다...
# 이런 방법이 아닌 뭔가 쌈빡한 방법있을것같은데...
# 마이너스 수의 최대값과 플러스 수의 최대값을 뽑아내서 그거에 맞게 배열을 생성하면 메모리를 줄일 수 있지않을까?


# python에서 절대값구하는 함수가 뭘까 -> abs()
# a의 b제곱 -> pow(a,b)

"""
import sys

n = int(sys.stdin.readline())
answer = [0] * n

for i in range(n):
    answer[i] = int(sys.stdin.readline())

answer.sort() # answer : 모든 카드의 숫자가 들어가 있다.
min_len = abs(answer[0])
max_len = answer[n-1]


min_result = [0] * (min_len + 1)
plus_result = [0] * (max_len + 1)

for i in answer:
    if i < 0:
        min_result[-i] += 1 # i가 마이너스니까
    else:
        plus_result[i] += 1


# 값이 제일 큰 수의 인덱스를 가져오면 된다.
# print(min_result)
# print(plus_result)

if max(min_result) > max(plus_result):
    print(-min_result.index(max(min_result)))
else:
    print(plus_result.index(max(plus_result)))
"""

# 이 방법으로 했을 때 powershell에서는 결과가 나오긴했다. 그 말은 list의 최대 배열은 지켰다는것.
# 그렇지만 백준에는 메모리 초과가 났다.
# 풀이 시간 1시간이 경과하여서 다른 풀이를 찾아보았다.
# 내가 조금 길게 풀었던 방식을 dictionary를 이용하면 더 짧고 편리하게 할 수 있었다.
# 근데 어쨌든 길게 적었어도 방식은 같다고 생각하는데 왜 메모리 초과가 날까?
# 이것이 단순히 list가 메모리를 잡아먹어서 인지 내 풀이가 잘못된것인지 궁금해서 질문을 남겨두었다.

import sys

n = int(sys.stdin.readline())
dic = {}

for val in range(n):
    tmp = int(sys.stdin.readline())
    if tmp in dic:
        dic[tmp] += 1
    else:
        dic[tmp] = 1

dic = sorted(dic.items(), key=lambda x: (-x[1], x[0]))

print(dic[0][0])