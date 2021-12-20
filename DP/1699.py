# 1699번

"""
# 시작 체크 리스트
1. 1시간이 지났으나 발상 불가 또는 아예 다른 길 0
2. 코드 50% 정도 완성
3. 1시간 보다 더 걸려서 코드 완성.
4. 코드는 다 돌아가는데 효율성에서 걸림.
5. 코드완성

# 완료 후 체크 리스트
1. 아예 모르겠음 0
2. 중간 정도 이해함.
3. 완벽히 이해함.
"""

# 직접 연습장에 적어보면서 규칙이 있는지를 보았다.
# 뭔가 규칙이 있는듯 없는 느낌인데. 생각하다보니 값을 저장하는 배열을 생성하여
# 입력값의 최대 갯수를 max로 뽑아내면 되겠다는 생각이 들었다.
# 문제는 4,9, 16같이 한가지 숫자의 배수가 문제엿다. 그부분을 어떻게 풀어야할까. math라이브러리를 사용해볼까
# math 라이브러리는 사용할 수 없다..
# max로 뽑아낸다고해도 복잡도가 O(n^2)이기 때문에 시간초과가 날것같다...다른 방법없을까

# 우선 dp라는 배열에 1의 제곱으로 구한 갯수를 저장하는 방법은 좀 신선했다.
# 왜 소스가 이렇게 적혀졌는지 이해했지만 왜 이런 규칙을 적용할 수 있는지는 아직 발견하지 못했다...
# 내일도 다시 봐야할 듯하다.

n = int(input())

inp = [i for i in range (n+1)]

for i in range(1, n + 1):
    for j in range(1, i):
        if (j * j) > i:
            break
        if inp[i] > inp[i - j * j] + 1:
            inp[i] = inp[i - j * j] + 1

print(inp[n])