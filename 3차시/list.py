#리스트
a=list() #빈 리스트 생성
a=[] #빈 리스트 생성(이 방법 더 많이 사용)
a=list(range(10)) #range() 함수를 이용하여 0~9까지 생성
print(a)

a=list('abcd')
print(a)

a=[1, 2, 3, 4]
print(len(a)) #리스트 요소의 개수
print(a[-1]) #마지막 요소의 음수 인덱스

a.append(5) #리스트의 마지막 위치에 5 추가
a.remove(3) #리스트에서 3삭제
print(a)

print(2 in a) #2는 a의 요소이므로 True 반환
print(6 in a) #6은 a의 요소가 아니므로 False 반환

print(min(a)) #리스트의 원소들 중 가장 작은 원소 반환
print(max(a)) #리스트의 원소들 중 가장 큰 원소 반환
print(sum(a)) #리스트 내의 원소의 값을 반환