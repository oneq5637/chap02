# -*- coding: utf-8 -*-
import sys

#p.99
#변수
#C나 자바와 같은 다른 언어와 달리 변수 선언 시 자료형을 입력할 필요가 없음
#C#과 자바스크립트에 var 타입
#php는 변수 선언 시 $로 통일함
#위의 언어들은 모두 값의 자료형을 자동으로 유추함

#파이썬은 변수 선언 시 자료형을 입력하지 않음
#파이썬은 모든 데이터형이 모두 객체형임
#파이썬은 자바와 달리 모든 자료형이 참조형

#파이썬은 모든 자료형이 참조형이기 때문에 참조하는 곳이 같은지 확인하는 is 명령어를 사용하여 확인함
#값을 확인해도 동일함
a = 3
b = 3
print("a와 b가 참조하는 곳이 같다 : {0}".format(a is b))
#a와 b가 참조하는 곳이 같다 : True

if (a == b):
    print("a와 b가 참조하는 곳이 같다")
else:
    print("a와 b가 참조하는 곳이 다르다")
#a와 b가 참조하는 곳이 같다

c = 3
print(sys.getrefcount(3))
print(sys.getrefcount(2))
d = 3
print(sys.getrefcount(c))
#참조하는 곳이 같아서 숫자가 계속 카운트 됨.
#이 함수를 쓰기 위해선 위에 import sys 작성할 것

#변수 선언의 여러가지 방법
#2개의 변수와 2개의 값을 동시에 선언하고 변수 하나에 하나의 값을 순서대로 대입 함
a,b = ("python", "life")
print(a)
print(b)
#python
#life

#변수를 튜플형태로 선언하고 값도 튜플 형태로 대입함
#튜플은 괄호를 입력하지 않아도 인식함
(a, b) = "python", "life"
print(a)
print(b)
#python
#life

#변수를 리스트 형태로 선언하고 값도 리스트 형태로 대입함
print()
[a, b] = ["python", "life"]
print(a)
print(b)
#python
#life

#변수를 2개 이상 선언하고 하나의 값으로 대입
print()
a = b = "python"
print(a)
print(b)
#python
#python

#변수의 값 스왑
#파이썬은 2변수의 값을 서로의 값으로 변경할 때 변환 함수를 만들 필요가 없음
#a = 10
#b = 20
#temp = 0

#temp = a   
#a = b     
#b = temp    

a = 3
b = 5
a,b = b, a
print("변수 a의 값 : {0}\n변수 b의 값 : {1}".format(a,b))
#변수 a의 값 : 5
#변수 b의 값 : 3

#변수 삭제하기
#del() 메모리에서 해당 변수를 삭제

a = 3
b = 3
print("a의 값은 : {0}".format(a))
print("b의 값은 : {0}".format(b))
print("a의 참조 카운트 : {0}".format(sys.getrefcount(a)))
print("b의 참조 카운트 : {0}".format(sys.getrefcount(b)))
del(a)
del(b)
#변수 a의 값 : 5
#변수 b의 값 : 3
#a의 값은 : 3
#의 값은 : 3
#a의 참조 카운트 : 42
#b의 참조 카운트 : 42
#del 함수를 사용하여 변수 a와 b를 삭제하여 변수 a와 b를 더 이상 사용할 수 없음
#print("del 사용 후의 a의 참조 카운트 : {0}".format(sys.getrefcount(a)))
#print("del 사용 후의 b의 참조 카운트 : {0}".format(sys.getrefcount(b)))

#리스트 복사
#리스트를 복사하는 일반적인 방법은 반복문을 사용하여 리스트의 내용을 다른 리스트에 대입하는 방법

#반복문을 사용하여 리스트 복사
a = [1,2,3]
print("원본 리스트 출력 : {0}".format(a))
#원본 리스트 출력 : [1, 2, 3]
b = a
#변수 b에 리스트 a를 대입
#변수 b에 리스트 값 [1,2,3]이 대입된 것이 아니라 변수 b에 리스트 a의 주소가 대입 됨
print("리스트 b 출력 : {0}".format(b))
#리스트 b 출력 : [1, 2, 3]
#리스트 a의 index 2의 값 수정
a[2] = 10
print("리스트 a 수정 후 출력 : {0}".format(a))
#리스트 a 수정 후 출력 : [1, 2, 10]#
#리스트 b의 요소를 수정하지 않았으나 리스트 a와 같이 값이 수정 됨
#변수 b에 리스트 a의 주소가 대입되었기 때문에 리스트 a의 요소가 수정되면 리스트 b의 요소도 함께 수정된 것처럼 보임
#이유는 동일한 주소를 참조하고 있기 때문
print("리스트 b 출력 : {0}".format(b))
#리스트 b 출력 : [1, 2, 10]

print()

#다른 언어에서 복사 함수를 사용하지 않고 배열이나 리스트를 다른 리스트로 복사하는 방법
count = 0
c = []
while(count < len(a)):
    c.append(a[count])
    count += 1

print("리스트 c 출력 : {0}".format(c))
#리스트 c 출력 : [1, 2, 10]
a[2] = 100
print("리스트 a 출력 : {0}".format(a))
print("리스트 b 출력 : {0}".format(b))
print("리스트 c 출력 : {0}".format(c))
#리스트 a 출력 : [1, 2, 100]
#리스트 b 출력 : [1, 2, 100]
#리스트 c 출력 : [1, 2, 10]

#파이썬의 리스트 출력 방식을 사용하여 리스트 a의 모든 값을 리스트 b로 복사
print()
a = [1,2,3]
b = a[:]
print("리스트 a 출력 : {0}".format(a))
print("리스트 b 출력 : {0}".format(b))
a[2] = 100
print("수정 후 리스트 a 출력 : {0}".format(a))
print("수정 후 리스트 b 출력 : {0}".format(b))
#리스트 a 출력 : [1, 2, 3]
#리스트 b 출력 : [1, 2, 3]
#수정 후 리스트 a 출력 : [1, 2, 100]
#수정 후 리스트 b 출력 : [1, 2, 3]


print()
from copy import copy
a = [1,2,3]
b = copy(a)
print("리스트 a 출력 : {0}".format(a))
print("리스트 b 출력 : {0}".format(b))
a[2] = 100
print("수정 후 리스트 a 출력 : {0}".format(a))
print("수정 후 리스트 b 출력 : {0}".format(b))
