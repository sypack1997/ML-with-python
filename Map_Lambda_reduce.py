# Lambda : 함수 이름 없이, 함수처럼 쓸 수 있는 익명함수
def f(x,y):
    return x+y
print(f(1,4)) # 5

f = lambda x,y: x + y
print(f(1,4))



# Map function : Sequence 자료형 각 element에 동일한 function을 적용함
# map(function_name, list_data)
ex  = [1,2,3,4,5]
f = lambda x: x ** 2
print(list(map(f,ex))) # [1, 4, 9, 16, 25]

f = lambda x, y: x + y
print(list(map(f, ex, ex))) # [2, 4, 6, 8, 10]

f = lambda x: x ** 2
print(map(f,ex)) # <map object at 0x0000014E356FFA30>
for i in map(f,ex):
    print(i) 
    # 1
    # 4
    # 9 --



# Reduce function : map function과 달리 list에 똑같은 함수를 적용해서 통합
from functools import reduce
print(reduce(lambda x,y: x+y, [1,2,3,4,5])) # 15