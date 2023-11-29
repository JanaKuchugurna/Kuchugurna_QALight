# file = open('example.txt', 'a', encoding='utf8')
# file.write('\nI add something\nThird line\nForth line')
# file.close()

# file = open('example.txt', 'r')
# data = file.read(8)
# print(data)
# file.close()



file = open('example.txt', 'r')
for line in file:
    print(line)
file.close()

