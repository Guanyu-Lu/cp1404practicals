"""
Word Occurrences
Estimate: 20 minutes
Actual:   18 minutes
"""
dictionary={}
texts=input("text: ").lower().strip().split(" ")
texts.sort()
print(texts)
for word in texts:
    if word not in dictionary.keys():
        dictionary[word]=1
    else:
        dictionary[word]+=1
print(dictionary)
word_width=max(len(word) for word in dictionary.keys())
for word,num in dictionary.items():
    print(f"{word:{word_width+1}}: {num}")