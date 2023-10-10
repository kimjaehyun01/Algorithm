#ch4 DIvide and Quenqer! 퀵정렬 구현하기
import random #pivot원소를 랜덤으로 뽑기위해 랜덤숫자 생성
#퀵정렬 함수
def quick_sort(list):
  #기본단계
  if len(list) < 2: 
    return list 
  #재귀단계 
  else: 
    num = random.randint(0,len(list)-1) #pivot원소를 랜덤으로 뽑기위해 랜덤숫자 생성
    pivot = list.pop(num)               #num인덱스의 원소값을 리스트에서 추출하면서 피벗값으로 지정
    less = [i for i in list[:] if i <= pivot] #피벗보다 작거나 같은 값을 less리스트에 저장

    bigger = [i for i in list[:] if i > pivot] #피벗보다 큰 값을 bigger리스트에 저장

    return quick_sort(less) + [pivot] + quick_sort(bigger)

print(quick_sort([55,23,28,1,100]))
