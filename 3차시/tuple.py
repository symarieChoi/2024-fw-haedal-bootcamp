#튜플: 리스트와 비슷하게 여러 개의 요소를 저장할 수 있으나 '불변'의 특징 지님(변경, 삭제, 추가 불가능)
tuple0=() #빈 튜플 만들기
tuple1=(1, ) #하나의 요소를 가진 튜플
tuple2 = (1, 2, 3) #여러 요소를 가진 튜플
tuple3 = ('apple', 1, 5, 5, [1, 2, 3]) #여러 자료형을 지닌 튜플

nums=[1, 2, 3]
tuple3=tuple(nums) #리스트를 튜플로 만들기
print(type(tuple3))
print(tuple3)

nums=(1, 2, 3, 4)
l_nums=list(nums) #튜플을 리스트로 만들기
print(type(l_nums))
print(l_nums)

l_nums[0]=100 #l_nums는 리스트이므로 요소 변경이 가능
print(l_nums)

#리스트와 동일하게 인덱스를 이용하여 자료에 접근 가능
nums=(1, 2, 3)
print(nums[0]) #인덱스 0번에 해당하는 값 반환
print(nums[1]) #인덱스 1번에 해당하는 값 반환

#리스트와 동일하게 덧셈과 곱셈 연산자가 정의됨(결과는 튜플로 반환)
a=(1, 2, 3)
b=(4, 5, 6)
print(a+b)
print(a*2)