# Asterisk : *를 의미, 단순곱셈, 제곱연산, 가변 인자 활용 등 다양하게 사용됨
def asterisk_test(a, *args):
    print(a, args) # 1(2, 3, 4, 5, 6)
    print(type(args)) # class tuple
asterisk_test(1,2,3,4,5,6)

def asterisk_test(a, **kargs):
    print(a, kargs) # 1 {'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}
    print(type(kargs)) # class dict
asterisk_test(1, b=2, c=3, d=4, e=5, f=6)



# Asterisk - unpacking a container
def asterisk_test(a, *args):
    print(a, args) # 1 (2, 3, 4, 5, 6)
    print(type(args)) # class tuple
asterisk_test(1,*(2,3,4,5,6))

def asterisk_test(a, args):
    print(a, *args) # 1 2 3 4 5 6  
    print(type(args)) # class tuple
asterisk_test(1,(2,3,4,5,6))

a,b,c = ([1,2], [3,4], [5,6])
print(a,b,c) # [1, 2] [3, 4] [5, 6]
data = ([1,2], [3,4], [5,6])
print(*data) # [1, 2] [3, 4] [5, 6]

def asterisk_test(a,b,c,d):
    print(a,b,c,d)
data = {"b":1, "c":2, "d":3}
asterisk_test(10, **data) # 10 1 2 3
asterisk_test(10, *data) # 10 b c d

for data in zip(*([1,2], [3,4], [5,6])):
    print(data)
    # (1, 3, 5)
    # (2, 4, 6)