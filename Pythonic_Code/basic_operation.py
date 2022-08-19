# iterable = [1,2,3,4]
# itertools.combinations(iterable, r) : iterable에서 원소 개수가 r개인 조합 뽑기. ex) r = 3 ---> (1,2,3), (1,2,4), (1,3,4), (2,3,4)

# itertools.combinations_with_replacement(iterable, r) : iterable에서 원소 개수가 r개인 중복 조합 뽑기. ex) r = 2 ---> (1,1), (1,2), (1,3), (1,4), (2,2), (2,3), (2,4), (3,3), (3,4), (4,4)

# itertools.perutations(iterable, r) : iterable에서 원소 개수가 r개인 순열 뽑기. ex) r = 2 ---> (1,2), (1,3), (1,4), (2,1), (2,3), (2,4), (3,1), (3,2), (3,4), (4,1), (4,2), (4,3)

# itertools.product(*iterables, repeat = 1) : 여러 iterable의 데카르트곱 변환. ex) iterator_1 = ['a', 'b', 'c'], iterator_2 = ['1', '2', '3'], repeat = 1 ---> ('a', '1'), ('a', '2'), ('a', '3'), ('b', '1'), ('b', '2'), ('b', '3'), ('c', '1'), ('c', '2'), ('c', '3')

# append vs extend
# list.append(x)는 리스트 끝에  1개를 그대로 넣는다. 
x = ['tick', 'tack', 'tok']
y = ['ping', 'pong']
x.append(y)
print(x) # ['tick', 'tack', 'tok', ['ping'], ['pong']]

x = ['tick', 'tack', 'tok']
y = 'ping'
x.append(y)
print(x) # ['tick', 'tack', 'tok', 'ping']

# list.extend(iterable)는 리스트 끝에 가장 바깥쪽 iterable의 모든 항목을 넣는다.
x = ['tick', 'tack', 'tok']
y = ['ping', 'pong']
x.append(y)
print(x) # ['tick', 'tack', 'tok', 'ping', 'pong']

x = ['tick', 'tack', 'tok']
y = 'ping'
x.append(y)
print(x) # ['tick', 'tack', 'tok', 'p', 'i', 'n', 'g']

# pop()함수는 리스트 내부 요소를 꺼내 주는 함수이다. 리스트에서 요소를 꺼내면서 그 요소는 리스트 안에서 지워진다.



import itertools
from functools import reduce
import sys
import time

def insert_operation(length, input_num, input_oper):

    ops = {"0": (lambda x,y: x+y), "1": (lambda x,y: x-y), "2": (lambda x,y: x*y), "3": (lambda x,y: x/y)}
    oper_permutation = []
    result = []
    list(oper_permutation.extend([str(index)]*value) for index, value in enumerate(input_oper) if value > 0)
    permutation = [list(x) for x in set(itertools.permutations(oper_permutation))]
    for i in permutation:
        result.append(reduce(lambda x,y : ops[i.pop()](x,y), input_num))
    
    print(str(max(result)) + "\n" + str(min(result)))


n = 6
numbers = [1,2,3,4,5,6]
arithmetics = [2,1,1,1]
insert_operation(n, numbers, arithmetics)