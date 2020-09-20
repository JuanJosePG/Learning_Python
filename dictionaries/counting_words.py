# Counting words in a text
counts=dict()
f_handler=open("Scripts/text.txt")

for line in f_handler:
    line=line.split() #list

    for word in line:
        counts[word]=counts.get(word,0)+1

print(counts)
