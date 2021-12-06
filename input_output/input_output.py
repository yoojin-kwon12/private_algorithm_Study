#1000번
a,b = input().split()
print(int(a)+int(b))

# 2558번
a = input()
b = input()
print(int(a) + int(b))


#10950번
n = input()
n = int(n)
a = [0] * n
b = [0] * n

for i in range(n):
    a[i], b[i] = input().split()

for i in range(n):
    print(int(a[i]) + int(b[i]))



# 10951번

while True:
    try:
        A, B = map(int,input().split())
        print(A+B)
    except:
        break

    while True:
        A, B = map(int, input().split())
        print(A + B)



# 10592번
while True:
    try:
        A, B = map(int, input().split())
        if A == 0 and B == 0:
            break
        else:
            print(A+ B)
    except:
        break


# 10953번

n = int(input())
A = [0] * n
B = [0] * n
for i in range(n):
    A[i],B[i] = input().split(',')

for i in range(n):
    print(int(A[i]) + int(B[i]))


# 11021번

n = int(input())
for i in range(n):
    a , b = map(int,input().split())
    print('Case #'+str(i+1)+':',a+b)



# 11022번

n = int(input())

for i in range(n):
    a,b = input().split()
    print('Case #'+ str(i+1)+': '+ a + ' + ' + b + ' = ' + str(int(a)+int(b)))



# 11718번

while True:
    try:
        str = input()
        print(str)
    except:
        break



# 11719번

while True:
    try:
        str = input()
        print(str)
    except:
        break


# 11720번

n = int(input())
a = list(map(int,input()))
print(sum(a))



# 11721번
# 배열로 각 글자를 넣어서 자른다...?
#    -> 배열로 굳이 넣지 않아도 됨. String은 배열처럼 index로 활용가능
#    -> 그리고 10개씩 자르는 방법을 for in range문 에서 range(0,길이, 10)으로 설정하면 됨.
# split을 이용해서 10개를 자르는 방법은 없는가?
#    -> slice를 사용

str = input()
length = len(str)

for i in range(0,length,10):
    print(str[i:i+10])



# 2741번

n = int(input())

for i in range(1,n+1,1):
    print(i)


# 2742번

n = int(input())

for i in range(n,0,-1):
    print(i)



# 2739번

n = int(input())

for i in range(1,10,1):
    print(str(n) + ' * ' + str(i) + ' = ' + str(n * i ))



# 1924번
# 달력 라이브러리가 있어야되는거아닌가...?
# -> 라이브러리 없어도 가능.
# input().split()의 타입은 list
day = 0

arrList = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
weakList = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]

x, y = map(int, input().split())


for i in range(x - 1):
    day = day + arrList[i]
day = (day + y) % 7

print(weakList[day])


import calendar

arrList = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
x, y = map(int,input().split())

Day = calendar.weekday(2007, x, y)
print(arrList[Day])



# 8393번
n = int(input())
answer = 0

for i in range(1,n+1):
    answer += i
print(answer)



# 10818번

n = int(input())
numbers = list(map(int,input().split()))

print(min(numbers),max(numbers))



# 2438번

n = int(input())

for i in range(1,n+1):
    print('*' * i)



# 2439번

n = int(input())

for i in range(1, n+1):
    print((' ' * (n-i)) + ('*' * i))



# 2440번

n = int(input())

for i in range(n, 0, -1):
    print('*' * i)


# 2441번

n = int(input())

for i in range(n,0,-1):
    print((' ' * (n-i)) + ('*' * i))



# 2422번

n = int(input())
star = [0] * n

for i in range(1, n + 1):
    star[i-1] = '*' * (2*i-1)

max_length = len(star[n-1])

# (max_length - 별갯수) // 2
for j in range(n):
    blank = ' ' * ((max_length - len(star[j])) // 2)
    print(blank + star[j])



N = int(input())

for i in range(1,N+1):

    b = ' '*(N-i)+'*'*((2*i)-1)
    print(b)



# 2445번
# 내방법
n = int(input())
front = [0] * n
back = [0] * n

# front / back
for i in range(1, n+1):
    front[i-1] = ('*' * i) + (' ' * (n - i))
    back[i-1] = (' ' * (n - i)) + ('*' * i)

for k in range(n):
    print(front[k] + back[k])

for g in range(n-2,-1,-1):
    print(front[g] + back[g])


# 다른 방법1

n = int(input())
a = 2*n
for i in range(1, n+1):
    print(('*'* i) + (' ' * (a-2*i)) + ('*'*i))
for j in range(n-1,0,-1):
    print(('*'* j) + (' ' * (a-2*j)) + ('*'*j))


# 2522번

n = int(input())

for i in range(1,n+1):
    print((' ' * (n-i)) + ('*' * i))
for j in range(n-1,0,-1):
    print((' ' * (n-j)) + ('*' * j))



# 2446번

n = int(input())

for i in range(n):
    print((' ' * i) + ('*'*(l-2*i)))
for j in range(n-2,-1,-1):
    print((' ' * j) + ('*'*(l-2*j)))


# 10991번
# 별표 + 공백 + 별표 + 공백 을 어떻게 표현하지...?
# "* "로 출력해야 된다는 사실은 알아차림...
n = int(input())

for i in range(1,n+1):
    print((' ' * (n-i)) + ('* ' * i))



# 10992번
# 내가 사용한 방법....하지만 틀림
n = int(input())

for i in range(1,n):
    print((' ' * (n-i)) + '*' + (' ' * (i-1)) + (' ' * (i-1)) + '*' )
print('*' * (2*n-1))


# 답들 보니 대부분 if문을 사용한다. if문을 사용해서 혼자 풀어보자.

n = int(input())

for i in range(1,n+1):
    if i ==1:
        print((' '* (n-1)) + '*')
    elif i == n:
        print('*' * (2 * n - 1))
    else:
        # 2*(i - 1)-1 이라는 식 기억해서 한번 대입해보기
        print((' ' * (n - i)) + '*' + (' ' * (2*(i - 1)-1)) + '*')







