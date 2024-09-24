fruits={'a':1000, 'b':2000, 'c': 3000}
fruits['d']=4000
print(fruits)
print(fruits['a'])

fruits['a']=100
print(fruits['a'])

del fruits['a'] #a 삭제
print(fruits)

fruits.pop('b') #b 삭제
print(fruits)

fruits['a']=1000 #다시 a 추가
print(fruits)

print(len(fruits)) #딕셔너리 항목의 개수를 반환

print('a' in fruits)

print('v' in fruits)