word_to_count = {}

text = input("Enter a sentence\n >>>")

words = text.split()

for word in words:
    amount = word_to_count.get(word, 0)
    word_to_count[word] = amount + 1


text = list(word_to_count.keys())
text.sort()

max_length = max((len(word) for word in text))
for word in text:
    print("{:{}} : {}".format(word, max_length, word_to_count[word]))
