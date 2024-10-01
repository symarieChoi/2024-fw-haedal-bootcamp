h, m = map(int, input().split()) #요리 시작 시간(시, 분)
t = int(input()) #요리하는 데 걸리는 시간(분)

m = m + t

if m >= 60:
    h = h + (m // 60)
    m = m % 60

if h > 23:
    h = h % 24

print(h, m)