def binary_search(data, key):
    data.sort() #data 오름차순 정렬
    #맨 왼쪽 위치
    start = 0
    #맨 오른쪽 위치
    end = len(data) - 1

    while start <= end:
        #중간 위치
        mid = (start + end) // 2

        if data[mid] == key:
            print("검색 성공!\n %d번 인덱스에 key 값이 존재합니다." %mid)
            return 0
        elif data[mid] > key:
            end = mid - 1
        elif data[mid] < key:
            start = mid + 1

    return 0

data = [5,3,4,7,8]
key = int(input())
binary_search(data, key)