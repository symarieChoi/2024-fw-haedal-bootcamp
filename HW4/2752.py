year = int(input())

x = year % 4
y = year %100
z = year % 400

if (x == 0) and (y != 0):
    print(1)
elif (x == 0) and (z == 0):
    print(1)
else:
    print(0)