# 11055번
# 가장 큰 증가 부분 수열
# 문제를 딱 봤을때 11053번의 문제에서 수열의 증가 부분 수열들의 값만 다 더하면 되지않을까..?라고 생각했다.
# 그럴 수가 없다는 사실을 깨달음.. max의 값을 출력했기때문에 따로 저장하는 수밖에 없다.
# 그리고 증가 부분이 길다고 해서 값이 크다는 보장이 없다. 예시를 대입해도 그렇다.

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

# answer = inp.copy() 부분을 answer = inp로 선언해서 계속 틀리게 답이 나옴.
# 확실히 기억되었다.

n = int(input())

inp = list(map(int, input().split()))

result = [1] * n # 증가 수열
# answer = [inp[0]] * n # 가장 큰 수
answer = inp.copy()

for i in range(1,n):
    for j in range(i):
        if inp[i] > inp[j]:
            result[i] = max(result[i], result[j] + 1)
            # print("inp[i] : " + str(inp[i]))
            # print("answer[j] : " + str(answer[j]))
            # print("answer[i] : " + str(answer[i]))
            answer[i] = max(answer[j] + inp[i], answer[i])

# print(result)
print(max(answer))

            

