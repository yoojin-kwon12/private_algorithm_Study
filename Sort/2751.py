# 2751번
# 참고 사이트 : https://chancoding.tistory.com/19
# https://velog.io/@yeseolee/Python-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%9E%85%EB%A0%A5-%EC%A0%95%EB%A6%ACsys.stdin.readline


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


"""
# input() 과 sys.stdin.readline()의 차이점 

input()은 prompt message를 parameter로 받을 수 있다. 그래서 해당 메시지를 출력해야되기 때문에 부하가 일어날 수도있다.
prompt message가 없는 경우도 있지만 이 경우도 부하로 작용할 수 있다. 

하지만 sys.stdin.readline()은 prompt message를 파라미터로 받지 않기 때문에 부하가 작용하지 않는다. 

python 2.x에는 input()과 raw_input()가 있었다. 
raw_input()은 입력값을 무조건 문자열로 받는다. 
input()은 데이터의 자료형을 자동으로 evalution하고 변수를 저장하기 때문에 raw_input()에 비해 상대적으로 느렸다.

python 3.x로 넘어오면서 raw_input()은 사라지고 input()이 raw_input()의 역할을 대신하여 입력값을 문자열로 받게 되었다. 
. 

"""

# 뭔가 sort()말고 다른 방법을 생각해보고 싶었는데 생각이 나지않았다. 오래 생각해도 생각해내지 못할 것같다.
# 입력받을 때, input()으로 입력받았다가 시간초과가 났다.
# 나는 뭔가 sort()말고 다른 방법을 사용해야 시간초과가 나지 않을 것이라고 생각했다.
# 다른 풀이 중, 나는 잘 모르는 sys.stdin.readline()을 쓴 방법을 보고 알아봐야겠다고 생각했다.
# 우선 input() 대신 적용해보니 시간초과는 나지 않았다.

import sys

n = int(input())
inp = []

for i in range(n):
    # 여러줄에 걸쳐서 입력받을때는 sys.stdin.readline()로 입력받아야 시간 초과가 나지않는다.
    # inp.append(int(input()))
    inp.append(int(sys.stdin.readline()))

inp.sort()

for j in range(n):
    print(inp[j])