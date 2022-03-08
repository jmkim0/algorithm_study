n = int(input())
words = set()
for i in range(n):
    words.add(input())

word_list = list(words)
word_list.sort(key= lambda x: (len(x), x))

for word in word_list:
    print(word)