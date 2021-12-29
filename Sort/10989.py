# 10989번

"""
# 시작 체크 리스트
1. 1시간이 지났으나 발상 불가 또는 아예 다른 길 0
2. 코드 50% 정도 완성
3. 1시간 보다 더 걸려서 코드 완성.
4. 코드는 다 돌아가는데 효율성에서 걸림.
5. 코드완성

# 완료 후 체크 리스트
1. 아예 모르겠음
2. 중간 정도 이해함.
3. 완벽히 이해함. 0
"""

# 이것 또한 효율성을 물어보는 문제 인것같다.
# 앞에서 봤듯이 파이썬에서 sort의 복잡도는 O(nlogn)이다.
# 그러면 복잡도는 70,000,000가 된다....음...일단 해보자

"""
import sys

n = int(input())
result = []

for i in range(n):
    result.append(int(sys.stdin.readline()))

result.sort()

for i in result:
    print(i)
"""

# 위의 방식으로 메모리 초과가 났다. (python 3, pypy3 둘다.)
# for문 속에서 append를 사용하게 되면 메모리 재할당이 이루어져서
# 메모리를 효율적으로 사용하지 못한다고 해서 수정해보았다.
# 그래도 메모리 초과

"""
import sys

n = int(input())
result = [0] * n

for i in range(n):
    result[i] = int(sys.stdin.readline())

result.sort()

for i in result:
    print(i)
    
"""

# 바꿀만한 부분은 다 바꿨는데 메모리 초과부분은 해결이 되지않아서 다른 풀이들을 보았다.
# 아애 다른부분으로 생각하고 있었다.
# 어차피 숫자를 오름차순으로 출력하기때문에 1부터 몇개가 나오는지만 체크하면 그대로 출력하면 되었다.

import sys

n = int(input())
result = [0] * 10001

for i in range(n):
    ex = int(sys.stdin.readline())
    result[ex] += 1

for i in range(10001):
    if result[i] > 0:
        for j in range(result[i]):
            print(i)
