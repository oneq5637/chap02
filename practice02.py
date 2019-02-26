# -*- coding: utf-8 -*-
print("문자열 1번")
pin = "881120-1068234"
yyyymmdd = pin[0:6]
num = pin[7:14]
print(yyyymmdd)
print(num)

print()

print("문자열 2번")
pin = "881120-1068234"
print(pin[7])

print()

print("리스트 1번")
a = [1,3,5,4,2]
a.sort()
a.reverse()
print(a)


print()

print("리스트 2번")
a = ['Life', 'is', 'too', 'short']
result = ' '.join(a)
print(result)

print("튜플 1번")
a = (1,2,3)
a = a + (4,)
print(a)



print()

print("딕셔너리 1번")
a = {'A':90, 'B':80, 'C':70}
result = a.pop('B')
print(a)
print(result)


print()


print("변수 1번")
a = b = [1,2,3]
a[1] = 4
print(b)
#b가 a의 리스트 주소를 참조하기 때문에 a 리스트의 값이 변경 되면 b의 리스트 값도 변경된다. 
