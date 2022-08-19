# 여러 단어들을 하나로 붙일 떄 1
colors = ['red', 'blue', 'green', 'yellow']
result = " "
for s in colors:
    result += s
print(result) # redbluegreenyellow

# 여러 단어들을 하나로 붙일 떄 2
colors = ['red', 'blue', 'green', 'yellow']
result = ''.join(colors)
print(result) # redbluegreenyellow