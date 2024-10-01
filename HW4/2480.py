a, b, c = map(int, input().split()) #주사위 세 개의 눈
price = 0 #상금

if (a == b) and (b == c):
    price = 10000 + (a * 1000)
elif  (a == b) or (b == c) or (a == c):
    if a == b:
        price = 1000 + (a * 100)
    elif b == c:
        price = 1000 + (b * 100)
    elif a == c:
        price = 1000 + (c * 100)
elif (a != b) and (b != c) and (a != c):
    if (a > b) and (a > c):
        price = a * 100
    elif (b > a) and (b > c):
        price = b * 100
    elif (c > a) and (c > b):
        price = c * 100

print(price)