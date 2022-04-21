# question 2

vocab = input("please enter your vocab : ")
inverseVocab = ""
n = len(vocab)
i = n-1
while i > 0 or i == 0:
    inverseVocab = inverseVocab+vocab[i]
    i = i-1

print(inverseVocab)