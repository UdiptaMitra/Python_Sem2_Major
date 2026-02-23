s1="HEllo WOrld"
s2="" #empty string
s3="\"hello\"" #using escape sequence
print(s3)
print(s1.upper()) #make upper case 
print(s1.lower()) #make lower case
print(s1.capitalize()) #capitralise first letter of whole sentence
print(s1.title()) #capitalize first letter of every word in sentence
print(s1.swapcase()) #upper to lower and vice versa in a string
s2=s1.replace("WOrld","my friend")
print(s2)
print(s2.find("my"))
print("we are"+" learning") #concatenation operation'''
str1=" we are learning python "
#print(str1[42]) - index out of range error
print(len(str1))#length of string
str2="""hello world
how are you""" #multuline string
print(len(str2)) #one extra count due to newline character \n
print(str1.strip())#right left side trailing spaces removed
print(str1.lstrip())#left side trailing spaces removed
print(str1.rstrip())#right side trailing spaces removed
word=str1.split(sep='e') #anything can be used as a delimiter
print(word) #list of splitted words
print(str1.count('a')) #frequency of the specified char
print(str1.isupper())
print(str1.islower())
print(str1.isalnum())
print(str1.isalpha())
print(str1.isascii())
print(str1.isdecimal())
print(str1.isdigit())
print(str1.isnumeric())
print(str1.istitle())
print(str1.isprintable())
print(str1.isidentifier())
print(str1.isspace())
print(str1.startswith(" we"))
