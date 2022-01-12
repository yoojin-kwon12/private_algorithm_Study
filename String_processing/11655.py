# 11655번

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

# 아스키코드로 풀면되겠다는 생각이 들었다.

# A의 아스키코드는 65 / 90
# 'a'의 아스키코드는 97 / 'z'는 122 / 총 26개
#  '1'의 아스키코드는 49/ '9'의 아스키코드는 57

# 처음에는 좀 중구난방으로 처리했다가 if문을 좀 정리했다.
# 이유는 모르겠는데 계속 틀렸다고한다.
# 이유를 찾아냈다 78인데 77이라고 하고있었다..
# 다른풀이에서 좀더 쉬운 방법도 찾아냈다


# 내 방법

import sys

n = sys.stdin.readline().replace("\n", "")
result = []

inp = list(n)
for i in inp:
    if 65 <= ord(i) <= 90 or 97 <= ord(i) <= 122:
        if 110 <= ord(i) <= 122 or 78 <= ord(i) <= 90:
            result.append(chr(ord(i) - 13))
        else:
            result.append(chr(ord(i) + 13))
    else:
        result.append(i)


print(''.join(result))

"""

# 초반에 했다가 틀린방법...조금 중구난방이다.
import sys

n = sys.stdin.readline().replace("\n", "")

result = []

inp = list(n)


for i in inp:
    if ord(i) == 32: # 공백
        result.append(i)
    elif 49 <= ord(i) <= 57: # string 형태의 숫자
        result.append(i)
    else:
        if ord(i) >= 110: # 소문자 O보다 큰거
            result.append(chr(ord(i) - 13))
            # print(result)
        elif 78 <= ord(i) <= 90: # 대문자 O보다 큰거
            result.append(chr(ord(i) - 13))
        else: # 그나머지 알파벳
            result.append(chr(ord(i) + 13))
            # print(ord(i))


print(''.join(result))


# 다른 풀이

n = input()
result = ""
inp = list(n)

for i in inp:
    if 'a' <= i <= 'z' or 'A' <= i <= 'Z':
        if 'n' <= i <= 'z' or 'N' <= i <= 'Z':
            result += chr(ord(i) - 13)
        else:
            result += chr(ord(i) + 13)
    else:
        result += i

print(result)

"""

