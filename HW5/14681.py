def find_quadrant(x, y):
    if x > 0 and y > 0:
        return "1"
    elif x < 0 and y > 0:
        return "2"
    elif x < 0 and y < 0:
        return "3"
    elif x > 0 and y < 0:
        return "4"
    
try:
    x = int(input())
    y = int(input())
    print(find_quadrant(x, y))
    
except ValueError:
    print("잘못된 입력입니다.")
except EOFError:
    print("입력이 예상치 못하게 종료되었습니다.")