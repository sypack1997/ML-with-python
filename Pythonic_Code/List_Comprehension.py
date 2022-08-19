# List Comprehensions 1-1
result = [i for i in range(10)]
print(result) # [1,2,3,4,5,6,7,8,9,10]

result = [i for i in range(10) if i % 2 == 0]
print(result) # [0,2,4,6,8]


# List Comprehensions 1-2
result = []
for i in range(10):
    result.append(i)
print(result) # [1,2,3,4,5,6,7,8,9,10]



# List Comprehensions 2-1
word_1 = "Hello"
word_2 = "World"
result = [i+j for i in word_1 for j in word_2] # Nested For loop (for loop안에 for loop를 또 넣는 것)
print(result) # ['HW', 'Ho', 'Hr', 'Hl', 'Hd', 'eW', 'eo', 'er', 'el', 'ed' ---]


# List Comprehensions 2-2
word_1 = "Hello"
word_2 = "World"
result = []
for i in word_1:
    for j in word_2:
        result.append(i+j)
print(result) # ['HW', 'Ho', 'Hr', 'Hl', 'Hd', 'eW', 'eo', 'er', 'el', 'ed', ---]



# List Comprehensions 3
case_1 = ["A", "B", "C"]
case_2 = ["D", "E", "A"]
result = [i+j for i in case_1 for j in case_2]
print(result) # ['AD', 'AE', 'AA', BD', 'BE', BA', ---]

result = [i+j for i in case_1 for j in case_2 if not(i ==j)]
print(result) # ['AD', 'AE', 'BD', 'BE', 'BA', 'CD', 'CE', 'CA']
result.sort()
print(result) # ['AD', 'AE', 'BA', 'BD', 'BE', 'CA', 'CD', 'CE']



# List Comprehensions 4
words = 'The quick brown fox jumps over the lazy dog'.split()
print(words) # ['The', 'quick', 'brown', 'fox', 'jumps', 'over', ---]
stuff = [[w.upper(), w.lower(), len(w)] for w in words] # list의 각 elemente들을 대문자, 소문자, 길이로 변환하여 two dimensional list로 변환
print(stuff) # [['THE', 'the', 3], ['QUICK', 'quick', 5], ['BROWN', 'brown', 5], ---]
for i in stuff:
    print(i)
    # ['THE', 'the', 3]
    # ['QUICK', 'quick', 5] ---



# Two dimensional vs One dimensional
case_1 = ["A", "B", "C"]
case_2 = ["D", "E", "A"]
result = [i + j for i in case_1 for j in case_2]
print(result)
result = [[i+j for i in case_1] for j in case_2]
print(result) # [['AD', 'BD', 'CD'], ['AE', 'BE', 'CE'], ['AA', 'BA', 'CA']]
