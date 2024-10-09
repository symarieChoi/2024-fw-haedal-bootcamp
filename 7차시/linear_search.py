def linear_search(data, key):
    i=0 #카운터용 변수
    while True:
        #검색 성공
        if data[i] == key:
            print("검색 성공!\nkey 값은 %d입니다." %data[i])
            break
        #검색 실패
        if i+1 == len(data):
            print("검색 실패!")
            break
        i += 1

data = [1, 2, 3, 4, 5]
key = 4
linear_search(data, key)