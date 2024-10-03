def max_of(a):
    maximum=a[0]

    for i in range(1, len(a)):
        if a[i] > maximum:
            maximum = a[i]
    return maximum


print("배열의 최댓값을 구합니다.")
n = int(input("원소 수를 입력하세요.:"))
x = [None] * n #배열 초기화

for i  in range(0, n):
    x[i] = int(input(f"x[{i}]값을 입력하세요.:"))

print(f"최댓값은 {max_of(x)}입니다.")