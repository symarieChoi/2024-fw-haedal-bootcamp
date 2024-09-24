#반복문 - for문
for i in range(5):
    print(i)

for i in range(1, 5):
    print(i)

for i in range(1, 5, 2):
    print(i)

total = 0
for i in range(1, 11):
    total+=i
print(total)

#i가 사용되지 않으면 i 생략 가능
for _ in range(10):
    print('hello') #range(10)이므로 0~9까지의 값을 가지면서 총 10번 명령 실행

#range() 함수: 0에서 n 이전까지의 정수를 차례로 생성
#range(start, stop, step): start에서 stop 이전까지 정수를 step 단위로 생성
#step 인자 생략하면 기본 1로 설정
#start 인자 생략하면 기본 0으로 설정
print(list(range(5))) #start(생략)=0, stop=5, step(생략)=1
print(list(range(1, 5))) #start=1, stop=5, step(생략)
print(list(range(1, 5, 2))) #start=1, stop=5, step=2
print(list(range(10, 100, 10))) #start=10, stop=100, step=10