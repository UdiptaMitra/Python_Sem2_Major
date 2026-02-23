#enter a sentence. using string and set operation find the unique words in a string
sent1=input("enter a sentence: ")
sent1=sent1.lower()
words=sent1.split() #words is list here
words=set(words)
print(words)