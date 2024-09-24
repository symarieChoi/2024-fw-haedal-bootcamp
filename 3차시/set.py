#집합
#다수의 자료를 저장 but 자료의 순서는 상관하지 않음
#중복된 자료 허용 X

set0 = set() #빈 집합 만들기 -> 딕셔너리와 구분짓기 위해 set()으로 빈 집합 형성
print(set0)

set1={1, 2, 3, 4} #중괄호를 이용하여 집합 선언
print(set1)

nums=(1, 2, 3, 4)
set2=set(nums) #튜플로 집합 선언
print(set2)

nums=[1, 2, 3, 4]
set3=set(nums) #리스트로 집합 선언
print(set3)