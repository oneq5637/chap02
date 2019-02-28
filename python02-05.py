# -*- coding: utf-8 -*-

#딕셔너리 사용하기
#key와 value로 구성되어 있는 자료형
#기존의 배열 및 리스트, 튜플은 index와 value로 구성되어 있는 형태의 자료형임
#index가 없기 때문에 자료의 저장 순서가 없음
#딕셔너리는 {}기호를 사용
#key와 value의 구분은 : 을 사용
#각 데이터의 구분은 ,로 구분함

dic = {"name":"pey", "phone":"012312313", "birth":"1228"}
print("딕셔너리를 사용한 자료형 : {0}".format(dic))
#딕셔너리를 사용한 자료형 : {'phone': '012312313', 'name': 'pey', 'birth': '1228'}
print("딕셔너리에서 원하는 값 출력 : {0}".format(dic["name"]))
#딕셔너리에서 원하는 값 출력 : pey

#리스트를 for문을 통하여 모든 값을 출력
testlist = ["pey", "010231231", "1118"]
for value in testlist :
    print(value)
#pey
#010231231
#1118

#딕셔너리의 값을 for문을 통하여 출력
for value in dic :
    print(dic[value])
#012312313
#pey
#1228

#자바의 경우 일반적인 for문으로 hashmap(딕셔너리)의 내용을 모두 출력할 수 없음
#foreach(향상된 for문)문을 상용하여 hashmap의 내용을 출력해야 함

#딕셔너리에 key와 value 추가하기
#변수 a에 딕셔너리를 직접 대입함
a = { 1 : "a"}
print("원본 딕셔너리 출력 : {0}".format(a))
#딕셔너리 변수 a에 a[key] = value형태로 값을 대입함
a[2] = "b"
print("추가된 딕셔너리 출력 : {0}" .format(a))
#원본 딕셔너리 출력 : {1: 'a'}
#추가된 딕셔너리 출력 : {1: 'a', 2: 'b'}
a[10] = "c"
print("다시 추가된 딕셔너리 출력 : {0}" .format(a))
#다시 추가된 딕셔너리 출력 : {1: 'a', 2: 'b', 10: 'c'}
a[10] = "10"
print("다시 또 추가된 딕셔너리 출력 : {0}" .format(a))
#다시 또 추가된 딕셔너리 출력 : {1: 'a', 2: 'b', 10: '10'}
a["list"] = [1,2,3,4,5]
print("딕셔너리의 요소로 리스트 추가 : {0}" .format(a))
#딕셔너리의 요소로 리스트 추가 : {1: 'a', 2: 'b', 'list': [1, 2, 3, 4, 5], 10: '10'}
a["tuple"] = ("a","b","c","d")
print("딕셔너리에 튜플 추가 : {0}" .format(a))
#딕셔너리에 튜플 추가 : {1: 'a', 2: 'b', 'list': [1, 2, 3, 4, 5], 10: '10', 'tuple': ('a', 'b', 'c', 'd')}


print()
#딕셔너리 요소 삭제
#del() 함수를 사용하여 딕셔너리의 요소 삭제
#del(dic[key])

del(a["tuple"])
del(a["list"])
print("del 함수를 이용하여 요소 삭제 : {0}" .format(a))
#del 함수를 이용하여 요소 삭제 : {1: 'a', 2: 'b', 10: '10'}

#딕셔너리 key 리스트 (keys)
#해당 딕셔너리의 key만 객체로 반환
dic = {"name":"pey", "phone":"012312313", "birth":"1228"}
print("keys 함수를 사용하여 딕셔너리의 key의 모음을 출력 : {0}" .format(dic.keys()))
#keys 함수를 사용하여 딕셔너리의 key의 모음을 출력 : ['phone', 'name', 'birth']

for k in dic.keys():
    print(k)
#phone
#name
#birth

print("dict_key 객체를 list로 변경 : {0}" .format(list(dic.keys())))
print("dict_key 객체를 tuple로 변경 : {0}" .format(tuple(dic.keys())))
#dict_key 객체를 list로 변경 : ['phone', 'name', 'birth']
#dict_key 객체를 tuple로 변경 : ('phone', 'name', 'birth')

#딕셔너리 value 리스트 (values)
print()
print("values를 이용하여 딕셔너리의 내용을 객체로 출력 : {0}" .format(dic.values()))
#values를 이용하여 딕셔너리의 내용을 객체로 출력 : ['012312313', 'pey', '1228']

#list함수와 tuple함수를 이용하여 형 변환
print("dict_values 객체를 list로 변경 : {0}".format(list(dic.values())))
print("dict_values 객체를 tuple로 변경 : {0}".format(tuple(dic.values())))
#dict_values 객체를 list로 변경 : ['012312313', 'pey', '1228']
#dict_values 객체를 tuple로 변경 : ('012312313', 'pey', '1228')

# 딕셔너리에서 key,Value 동시에 얻기(items)
print("items 함수를 이용하려 dict_items 객체 얻기 : {0}".format(dic.items()))
#items 함수를 이용하려 dict_items 객체 얻기 : [('phone', '012312313'), ('name', 'pey'), ('birth', '1228')]
print("dict_items 객체를 list로 변경 : {0}".format(list(dic.items())))
#dict_items 객체를 list로 변경 : [('phone', '012312313'), ('name', 'pey'), ('birth', '1228')]

#딕셔너리 내용 삭제  (clear)
print()
print("원본 딕셔너리 출력 : {0}".format(dic))
print("clear 함수를 이용하여 딕셔너리 삭제 : {0}".format(dic.clear()))
#원본 딕셔너리 출력 : {'phone': '012312313', 'name': 'pey', 'birth': '1228'}
#clear 함수를 이용하여 딕셔너리 삭제 : None

#딕셔너리 key를 이용하여 value 얻기 (get)
#기존의 딕셔너리 value 사용 방법인 dic[key]와 결과값은 동일하지만 dic[key] 방식은 없는 키를 통해서 value를 호출하면 에러가 발생하지만 get 함수를 사용 시 없는 키를 통하여 value를 호출하면 None이 출력 됨
print()
dic = {"name":"pey", "phone":"012312313", "birth":"1228"}
print("dic.get(key) 방식으로 없는 키 사용 : {0}" .format(dic.get("tel")))
print("dic[key] 방식으로 없는 키 사용 : {0}".format(dic["tel"]))
#dic.get(key) 방식으로 없는 키 사용 : None
#Traceback (most recent call last):
#  File "python02-05.py", line 114, in <module>
#    print("dic[key] 방식으로 없는 키 사용 : {0}".format(dic["tel"]))
#KeyError: 'tel'


#자료형의 참과 거짓
#문자열은 빈 문자열이 아니면 true, 빈 문자열은 false
#리스트는 빈 리스트가 아니면 true, 빈 리스트면 false
#튜플은 리스트와 동일
#딕셔너리도 리스트와 동일
#숫자형은 0이 아닌 모든 수는 true, 0은 false
#값 None는 false
print()
