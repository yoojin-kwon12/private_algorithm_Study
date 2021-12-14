# 9465번

"""
# 시작 체크 리스트
1. 1시간이 지났으나 발상 불가 또는 아예 다른 길 0
2. 코드 50% 정도 완성
3. 1시간 보다 더 걸려서 코드 완성.
4. 코드는 다 돌아가는 효율성에서 걸림.
5. 코드완성

# 완료 후 체크 리스트
1. 아예 모르겠음
2. 중간 정도 이해함.
3. 완벽히 이해함.0
"""


"""

T = int(input())
num = []
for i in range (T):
    n = int(input())

    for j in range(n):
        num.append(int(input().split()))
print(num)
dx = [-1,0,1,0]
dy = [0,1,0,-1]

def make_zero():

    for i in range(4):
"""

# 점점 더해가면 dp가 적용 가능한지 생각해볼것.
# 점점 더해져가는데 더해지는 것에 규칙성이 있다면  dp가 가능함.
# input().split() 의 결과값이 list로 나온다는 사실을 깨달음.
# map 함수가 map(function,iterable)이라는 사실...을 까먹엇음.



T = int(input())
for i in range(T):
    s = []
    n = int(input()) # n열
    for j in range(2):
        # print(input().split())
        s.append(list(map(int,input().split())))

    for p in range(1,n):
        if p == 1:
            s[0][1] += s[1][0]
            s[1][1] += s[0][0]
        else:
            s[0][p] += max(s[1][p-2],s[1][p-1])
            s[1][p] += max(s[0][p-2],s[0][p-1])
    print(max(s[0][n-1],s[1][n-1]))
















