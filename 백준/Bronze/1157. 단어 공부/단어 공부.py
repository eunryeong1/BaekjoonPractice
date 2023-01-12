word = input().lower()
word_spelling = list(set(word))

count_list = []
for i in word_spelling:
  counts = word.count
  count_list.append(counts(i))

if count_list.count(max(count_list)) > 1:
  print("?")

else:
  print(word_spelling[(count_list.index(max(count_list)))].upper())