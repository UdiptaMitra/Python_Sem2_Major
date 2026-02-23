#wap to take one sentence from user and list out the unique words in that sentence
str=input("enter a string: ")
words=str.split()
words=set(words)
print(words)