#리스트의 메소드
a=[2, 4, 1, 7, 8, 11, 11, 11]
print(a.index(2)) #리스트에서 요소 2의 인덱스값 반환
print(a.count(2)) #리스트에서 요소 2의 개수 반환
print(a.count(11))

a.insert(0, 100) #리스트의 0번째 자리에 100 추가
print(a)

a.pop() 
print(a)

a.pop(0) #index 위치의 원소를 삭제 후 반환
print(a)

a.sort() #오름차순
print(a)

a.sort(reverse=True) #내림차순
print(a)

#리스트의 연산
a = [1, 2, 3]
b = [4, 5, 6]
print(a+b)

a = [1, 2, 3]
print(a*2)

print(a==b)

a = [1, 2, 3]
b = [1, 2, 3, 4]
print(a<b) #리스트의 사전식 비교