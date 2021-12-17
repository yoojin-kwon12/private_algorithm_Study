# 11054번
# 가장 긴 바이토닉 부분 수열


"""
# 시작 체크 리스트
1. 1시간이 지났으나 발상 불가 또는 아예 다른 길
2. 코드 50% 정도 완성
3. 1시간 보다 더 걸려서 코드 완성. 0
4. 코드는 다 돌아가는데 효율성에서 걸림.
5. 코드완성

# 완료 후 체크 리스트
1. 아예 모르겠음
2. 중간 정도 이해함.
3. 완벽히 이해함. 0
"""

# 이전 문제의 응용 문제라는 것 알겠다.
# inp[i]를 기준으로 inp[i-1], inp[i-2] ,inp[i-3] ...를 비교할 때, 작은수/ 큰수 전부다 비교하면 될것같다.
# 근데 무엇을 기준으로 up과 down을 나눌것인가?
# 계속 커지다가 한번 작아지고나면 다시 커지면 안됨.
# 계속 작아지다가 한번 커지고나면 다시 작아지면 안됨.
# UP(커지는것) DOWN(작아지는것) 따로따로 가장 긴 수를 찾아보자. 두개를 더했을때 가장 긴 결과가 답이지않을까
# UP(커지는것) DOWN(작아지는것)중에 하나가 정방향(왼 -> 오)이면 하나는 반대방향 (오 -> 왼)이어야 하지않나..?
# 아 down - up은 없고 무조건 up - down이구나 그게 바이토닉 수열이구나


n = int(input())
answer = [0] * n

# 입력 배열과 입력 배역의 역순
inp = list(map(int, input().split()))
# list형을 역순으로 하기 위해서는 [::-1]이 필요함.
inp_reverse = inp[::-1]

result = [1] * n
result_reverse = [1] * n

for i in range(1, n):
    for j in range(i):
        if inp[i] > inp[j]:
            result[i] = max(result[i], result[j] + 1)
        if inp_reverse[i] > inp_reverse[j]:
            # 처음에 result_reverse[i] 를 result_reverse로 적어서 오류가 남.
            result_reverse[i] = max(result_reverse[i], result_reverse[j] + 1)

result_reverse = result_reverse[::-1]
# print(result)
# print(result_reverse)
for i in range(n):
    # -1을 빼는 것은 뭔가 왠지 빼야될것같아서 한번 빼봤는데 정답이었다.
    # 다시 자세히 생각해보니 result_reverse[i] + result[i]하면 동일한 값이 두번 더해지는게 되므로 한번을 뺐다
    answer[i] = result_reverse[i] + result[i] -1

print(max(answer))














