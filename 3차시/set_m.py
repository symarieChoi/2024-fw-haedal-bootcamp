#집합의 메소드와 연산
s=set()
s.add(1) #빈 집합 s에 1 추가
s.add(2) #집합 s에 2 추가
s.add(100) #집합 s에 100 추가
print(s)

s.remove(100) #집합 s에서 100 삭제
print(s)

a={1, 2, 3}
b={3, 4, 5}
print(a|b) #합집합 연산
print(a.union(b)) #메소드 이용하여 합집합 반환
print(a-b) #차집합 연산
print(a.difference(b)) #메소드 이용하여 차집합 반환
print(a&b)
print(a.intersection(b)) #메소드 이용하여 교집합 반환