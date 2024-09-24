#딕셔너리의 메소드
fruits = {'a':1000, 'b': 2000, 'c': 3000}
print(fruits.keys()) #딕셔너리의 모든 key값 반환

print(fruits.values()) #딕셔너리의 모든 value값 반환

print(fruits.get('a')) #딕셔너리의 a값 반환(딕셔너리에 없는 키 => None 반환)

print(fruits.pop('a')) #키에 대한 값 반환 후 삭제
print(fruits)

print(fruits.clear()) #딕셔너리의 모든 요소 삭제