# 10820번

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
3. 완벽히 이해함. 0
"""

# A의 아스키코드는 65 / 90
# 'a'의 아스키코드는 97 / 'z'는 122
# str(type(i)) == "<class 'int'>": 를 활용해서 타입으로 검사를 하려고 했다.
# 입력이 애초부터 string으로 되기때문에 1이 들어와도 '1'로 들어온다는 문제가 있었다.

# 위의 방법보다 아스키코드를 활용한 방법이 맞겠다 싶어서 풀었고
# 입력값의 갯수가 정해져있지 않았기때문에 while문을 사용했다.
# 제출하니 입력초과가 나왔다.
# 다른 풀이를 찾아보니 if not n:  break 를 활용하여 입력이 없으면 break처리를 해주어야했다.

##### 알게된것 정리

# 1. 타입검사 함수 : type()
# 2. sys.stdin.readline()에서 뒤에 strip() 을 붙이면 앞뒤 모든 공백이 제거된다.
#    뒤의 공백이 필요하지만 엔터는 제거해야 될 때
#    strip()이 아닌 replace("\n","") 나 rstrip("\n") 을 사용한다.
# 3. 입력값의 갯수가 정해져있지 않을때는 if not n : break 를 사용하여 입력이 없을땐 break를 걸어야한다.


import sys

while True:
    n = sys.stdin.readline().replace("\n", "")
    # [소문자의 갯수, 대문자의 갯수, 숫자, 공백
    inp = [0] * 4

    if not n:
        break
    for i in n:

        if 48 <= ord(i) <= 57:
            inp[2] += 1
        elif 65 <= ord(i) <= 90:
            inp[1] += 1
        elif 97 <= ord(i) <= 122:
            inp[0] += 1
        else:
            inp[3] += 1

    print(' '.join(map(str, inp)))

