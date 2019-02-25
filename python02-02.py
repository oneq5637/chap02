# -*- coding: utf-8 -*-
# 문자열 사용하기
# 파이썬은 문자 타입과 문자열 타입의 구분이 없음
# 문자열은 ""로 감싼 문자는 모두 문자열로 표현
# 문자열로 표시 문자 "", '', """ """, ''' ''' 총 4개의 타입이 존재함

print("문자열 출력하기")
print("\" 를 통해서 문자열 출력")
print('\' 를 통해서 문자열 출력')
#문자열 출력하기
#" 를 통해서 문자열 출력
#' 를 통해서 문자열 출력

str = """ 쌍따옴표를 3개 사용하는 방식은 
입력하는 그대로
화면에 출력하기 위해서 임"""
print(str)
#쌍따옴표를 3개 사용하는 방식은 
#입력하는 그대로
#화면에 출력하기 위해서 임

str = ''' 홀따옴표를 3개 사용하는 방식도
입력하는 그대로 
            화면에 출력하기 위해서임'''
print(str)
# 홀따옴표를 3개 사용하는 방식도
#입력하는 그대로 
#            화면에 출력하기 위해서임

# 문자열 사용시 이스케이프 문자 사용 가능
# \n : 문자열 안에서 줄 바꿈을 실행
# \t : 문자열 안에서 tab 키를 누른 효과
# \a : 컴퓨터에서 알람 효과
# \b : 백스페이스바 키 누른 효과
# \" : 문자열 안에서 문자로서의 "를 출력
# \' : 문자열 안에서 문자로서의 '를 출력
# \\ : 문자열 안에서 문자로서의 \를 출력
# \000 : 널문자 출력

multiline = "Life is to sholt\nyou need python"
print(multiline) 
#Life is to sholt
#you need python

multiline = "Life is to sholt\fyou need python"
print(multiline) 
#Life is to sholt
#                you need python

# 문자열 연산
# 파이썬은 다른 언어와 달리 여러가지 연산자를 지원함
# +, *
# + : 다른 언어와 같은 기능을 하는 연산자로 문자열끼리 연결시켜 하나의 문자열로 만듬
# * : 다른 언어에는 없는 기능으로 문자열을 반복해서 출력할 수 있는 기능을 지원함

head = "Python"
tail = "is fun!"
print(head + tail)
#Pythonis fun!

a = "python"
print(a * 2)
#pythonpython

print("=" * 50)
print("My Program")
print("=" * 50)
#==================================================
#My Program
#==================================================

# 문자열 인덱싱 
# 문자열은 문자 타입의 배열과 같다
# 시작 인덱스는 0임
# 해당하는 위치의 인덱스 번호를 사용하면 그 위치의 문자를 알 수 있음
# 자바에서 배열을 사용하듯이 파이썬에서도 사용할 수 있음
# a = "my first python program"
# 위와 같은 문자열이 있을 때 y를 출력하고 싶은 경우 배열처럼 변수명[index]로 사용 함
# a[10]

a = "my first python program"
print(a[10])
#y

#문자 슬라이싱
# 파이썬에서 문자열 처리 시 특정 위치의 글자를 출력할 때 엑셀에서 특정 셀 범위 설정하는 방법과 같이 사용이 가능 함
# a[시작번호:끝번호]
# a[0:10]
# 문자열 변수 a에서 인덱스번호 0 ~ 10까지의 문자를 출력함
print(a[0:10])
#my first p

#자바에서는 Substring, split 이라는 메서드를 사용하여 문자열을 잘라서 특정 위치의 문자열을 가지고 와야 하지만 파이썬에서는 문자 슬라이싱을 통해서 쉽게 구현이 가능하다.
print(a[9:15])
#python

# 문자열 슬라이싱 시 시작 번호나 끝 번호를 입력하지 않으면 처음부터 끝 번호까지 출력하거나, 시작번호부터 끝까지 출력함
print(a[:15])
print(a[15:])
#my first python
# program

#변수와 함께 사용 시 원하는 부분을 글자만 변수에 저장이 가능함
b = a[:15]
c = a[15:]
d = a[9:15]
print(b)
print(c)
print(d)
#my first python
# program
#python

print("=" * 100)
print()

#문자열 포매팅
#문자열을 화면에 출력할때 문자열 포맷을 통하여 사용자가 원하는 형태로 출력할 수 있음
#문자열 포맷 코드
# $s : 문자열 출력
# $c : 문자 1개 출력
# $d : 정수 출력
# %f : 실수 출력
# %o : 8진수 출력
# %x : 16진수 출력
# %% : 문자 % 출력

# %s는 해당 위치에 문자열을 출력함
# 어떠한 타입의 값도 모두 문자열로 출력함

print("i have %d apples" % 3) #정수인 3을 %d에 대입
print("i have %s apples" % 3) #정수인 3을 문자열로 변환하여 %s에 대입
print("rate is %f" % 3.234) #실수인 3.234를 %f에 대입
print("rate is %s" % 3.234) #실수인 3.234를 문자열로 변환하여 %s에 대입
#i have 3 apples
#i have 3 apples
#rate is 3.234000
#rate is 3.234

#문자열에 %문자를 출력할 경우 %%를 2번 입력한다
print("Error is %d%%." % 98)
#Error is 98%.

#문자열 출력 코드 %s에 총 문자열의 크기를 입력하여 표시하면 입력한 문자열의 크기만큼 글자가 입력됨
#-부호가 있을 경우 왼쪽 정렬, 없을 경우 오른쪽 정렬
print("%10s jane" % "hi!")
print("%-10s jane" % "hi")
#       hi! jane
#hi         jane

#숫자형에도 %와 기호 사이에 범위 숫자를 입력하면 그 길이만큼 숫자의 자리를 확보함
print("%0.4f" % 3.42134234)
print("%10.4f" % 3.42134234)
#3.4213
#    3.4213

#파이썬 문자열 함수
#count() : 문자 개수 확인
#len() : 문자 길이 
#find() : 문자 위치 확인
#join() : 문자 삽입하기
#upper() : 영문 소문자를 대문자로 변경
#lower() : 영문 대문자를 소문자로 변경
#strip() : 문자열 양쪽 공백 삭제
#replace() : 문자열 변경하기
#split() : 문자열 나누기

a = "hobby"
print("문자열에서 b의 개수 확인 : %s" % a.count('b'))
#문자열에서 b의 개수 확인 : 2

print("문자열 길이 확인 : %s" % len(a))
#문자열 길이 확인 : 5

a = "Python is best choice"
print("문자 'b'가 처음 나온 위치는 : %s" % a.find('b'))
#문자 'b'가 처음 나온 위치는 : 10








# 2019-02-25 수업내용

#개념적인 부분보다 외워야하는 부분이 많음
#p.60

a = ","
print(a.join('abcd'))       
# a,b,c,d

a = "hi"
print(a.upper())        
# HI

a = "hi"
print(a.lower())        
# hi

a = "     hi"
print("원본 문장 : %s" % a)
print("왼쪽 공백 지우기 : %s" % a.lstrip())
# 원본 문장 :      hi
# 왼쪽 공백 지우기 : hi

a = "hi     "
print("원본 문장 : %s" % a)
print("오른쪽 공백 지우기 : %s" % a.rstrip())
# 원본 문장 : hi
# 왼쪽 공백 지우기 : hi

a = "       hi     "
print("원본 문장 : %s" % a)
print("양쪽 공백 지우기 : %s" % a.strip())
# 원본 문장 :        hi
# 양쪽 공백 지우기 : hi

a = "Life is too short"
print("원본 문장 : %s" % a)
print("수정된 문장 : %s" % a.replace("Life","Your leg"))
#원본 문장 : Life is too short
#수정된 문장 : Your leg is too short

#split()를 사용하면 지정한 문자로 문자열을 나누어서 문자열 배열에 출력함
a = "Life is too short"
print("원본 문장 : %s" % a)
print("수정된 문장 : %s" % a.split())
#원본 문장 : Life is too short
#수정된 문장 : ['Life', 'is', 'too', 'short']

a = "a:b:c:d"
print("원본 문장 : %s" % a)
print("수정된 문장 : %s" % a.split(':'))
#원본 문장 : a:b:c:d
#수정된 문장 : ['a', 'b', 'c', 'd']

print()
print("=" * 50)
print()

test = 10.0
print("화면에 출력한 코드 %f" % test)
print("화면에 출력한 코드 %d" % test)
#화면에 출력한 코드 10.000000
#화면에 출력한 코드 10


# 문자열 코드를 사용하지 않고 format()함수를 이용하여 문자열을 형식에 맞춰 출력
# 문자열 코드 대신 {0}을 사용하여 각종 데이터가 들어갈 부분을 표현
# 입력될 데이터가 여러개일 경우 {0} {1} {2} {n} 으로 표현 
# 값은 foramt(첫번째값, 두번째값 , 세번째값, n번째값)으로 데이터를 입력
print(".format() 함수를 이용하여 문자열을 쉽게 표현하기")

#숫자 대입하기
print("I eat %d apples" % 3)
print("I eat {0} apples".format(3))
#I eat 3 apples
#I eat 3 apples

#문자열 대입하기
print("I eat %s apples" % "five")
print("I eat {0} apples".format("five"))
#I eat five apples
#I eat five apples

#변수 대입하기
number = 3
print("I eat %d apples" % number)
print("I eat {0} apples".format(number))
#I eat 3 apples
#I eat 3 apples

#정수와 실수 대입하기
# %d와 %s를 헷갈릴 우려가 있음
number1 = 100
number2 = 100.0
print("정수 출력 : %d, \n소수 출력 : %f" %(number1,number2))
#정수 출력 : 100, 
#소수 출력 : 100.000000

print("정수 출력 : {0}, \n소수 출력 : {1}" .format(number1,number2))
#정수 출력 : 100, 
#소수 출력 : 100.0


#2개 이상의 값 넣기
number = 10
day = "three"
print("I ate {0} apples. so I was sick for {1} days" .format(number,day))
#I ate 10 apples. so I was sick for three days


#format() 함수 사용시 {index} 대신 {변수이름}으로 사용가능. 직관적이다.
print("I ate {number} apples. so I was sick for {day} days." .format(number=10,day=3))
#I ate 10 apples. so I was sick for 3 days.

#{index}와 {변수이름}을 동시에 혼용해서 사용가능함
print("I ate {0} apples. so I was sick for {day} days." .format(10,day=3))
##I ate 10 apples. so I was sick for 3 days.

#문자열 왼쪽 정렬
print("문자열 왼쪽 정렬 : %-10s jane" % "hi")
print("문자열 왼쪽 정렬 : {0:<10} jane".format("hi"))
#문자열 왼쪽 정렬 : hi         jane
#문자열 왼쪽 정렬 : hi         jane      

print("문자열 오른쪽 정렬 : %10s jane" % "hi")
print("문자열 오른쪽 정렬 : {0:>10} jane".format("hi"))
#문자열 오른쪽 정렬 :         hi jane
#문자열 오른쪽 정렬 :         hi jane

print("문자열 중앙 정렬 : {0:^10} jane".format("hi"))
#문자열 중앙 정렬 :     hi     jane

#공백 채우기
print("문자열 공백 채우기 : {0:=^10} jane".format("hi"))
#문자열 공백 채우기 : ====hi==== jane

print("문자열 공백 채우기 : {0:!<10} jane".format("hi"))
#문자열 공백 채우기 : hi!!!!!!!! jane

print("문자열 형식 채워서 표현하기 : {0:0>10}".format(100))
#문자열 형식 채워서 표현하기 : 0000000100

# 소수점 표현하기
y = 3.42134234
print("소수점 4자리까지 표현 : {0:0.4f}".format(y))
#소수점 4자리까지 표현 : 3.4213

print("소수점 5자리까지 표현,전체자리수는 10자리로 표현 : {0:10.5f}".format(y))
#소수점 5자리까지 표현,전체자리수는 10자리로 표현 :    3.42134

# 문자 {} 표현하기
print("{{and}}".format())
#{and}











