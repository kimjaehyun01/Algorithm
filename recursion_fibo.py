#chap3 재귀함수
#재귀함수로 피보나치수열 구현하기
def fib(n):
    if n == 0:                #기본단계1
        return 0
    elif n == 1 or n == 2:    #기본단계2
        return 1
    else:                    #재귀단계
        return fib(n - 1) + fib(n - 2)

for i in range(1,11):
  print(fib(i))
