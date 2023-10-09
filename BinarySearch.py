#chap1 이진탐색
def BinarySearch(list, num):
    list.sort()
    low = 0
    high = len(list) - 1
    trying = 1
    while low <= high:
        mid = (low + high) // 2     #리스트의 중간인덱스
        guess = list[mid]
        if num > guess:     #guess가 리스트의 중간값보다 크면
            low = mid+1
        elif num < guess:   #guess가 리스트의 중간값보다 작으면
            high = mid
        else:               #guess가 리스트의 중간값과 같으면
            print(f"숫자는 {guess}입니다! 추측횟수는 {trying}번 입니다.")
            return None
        trying += 1
    print("찾으려는 숫자가 리스트안에 없습니다.")
    return None

list1 = [x for x in range(0,10001)]
num1 = 10000

BinarySearch(list1, num1)
