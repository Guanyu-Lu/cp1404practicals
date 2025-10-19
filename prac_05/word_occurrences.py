"""
Word Occurrences
Estimate: 20 minutes
Actual:   18 minutes
"""
word_to_count={}
texts=input("text: ").lower().strip().split(" ")
texts.sort()
print(texts)
for word in texts:
    word_to_count[word] = word_to_count.get(word, 0) + 1
print(word_to_count)
word_width=max(len(word) for word in word_to_count.keys())
for word,num in sorted(word_to_count.items()):
    print(f"{word:{word_width+1}}: {num}")