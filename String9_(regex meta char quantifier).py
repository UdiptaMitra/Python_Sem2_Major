'''Meta characters
. Any character (except newline character) 
^ Starts with 
\$ Ends with 
* Zero or more occurrences 
+ One or more occurrences 
{ } Exactly the specified number of occurrences 
[] A set of characters 
\ Signals a special sequence (can also be used to escape special characters)
| Either or 
( ) Capture and group'''
import re
test_string = 'python-engineer\n.com'
pattern = re.compile(r'\.') #\. means to exactly find match of fulolstop
matches = pattern.finditer(test_string)
for match in matches:
    print(match)
    
print()
pattern = re.compile(r'.') #match any character except newline
matches = pattern.finditer(test_string)
for match in matches:
    print(match)
print()

'''Special Sequences

\d :decimal digit [0-9].
\D : non-digit character [^0-9].
\s : whitespace
\S : non-whitespace
\w : alphanumeric (word) character [a-zA-Z0-9_].
\W : non-alphanumeric character [^a-zA-Z0-9_].
\b Returns a match where the specified characters are at the beginning or at the end of a word r"\bain" r"ain\b"
\B Returns a match where the specified characters are present, but NOT at the beginning (or at the end) of a word r"\Bain" r"ain\B"
\A Returns a match if the specified characters are at the beginning of the string "\AThe"
\Z Returns a match if the specified characters are at the end of the string "Spain\Z"'''

test_string = 'hello 123_ heyho hohey'

pattern = re.compile(r'\d') #number
matches = pattern.finditer(test_string)
for match in matches:
    print(match)
print()

pattern = re.compile(r'ABC$') #at the end
matches = pattern.finditer("123abc456abc_ABC")
for match in matches:
    print(match)
print()

pattern = re.compile(r'\s') #space
matches = pattern.finditer(test_string)
for match in matches:
    print(match)
print()

pattern = re.compile(r'\w') #alphanmum no whitespace
matches = pattern.finditer(test_string)
for match in matches:
    print(match)
print()

pattern = re.compile(r'\bhey') #begin or end of word
matches = pattern.finditer('heyho hohey') # ho-hey, ho\nhey are matches! (any delimeter)
for match in matches:
    print(match)
print()

pattern = re.compile(r'\Ahello') #beginning of string
matches = pattern.finditer(test_string)
for match in matches:
    print(match)
print()

pattern = re.compile(r'123_\Z') #end of string
matches = pattern.finditer(test_string)
for match in matches:
    print(match)
print()

pattern = re.compile(r'[a-zA-Z]') #occurances of the given set of alphabets
matches = pattern.finditer(test_string)
for match in matches:
    print(match)
print()

pattern = re.compile(r'[lo]') #occurances of these individual chars
matches = pattern.finditer(test_string)
for match in matches:
    print(match)
print()

pattern = re.compile(r'[0-9-]') #occurances of the given set of numbers and a dash
matches = pattern.finditer("helllo 123-")
for match in matches:
    print(match)
print()

'''quantifiers
* : 0 or more
+ : 1 or more
? : 0 or 1, used when a character can be optional
{4} : exact number
{4,6} : range numbers (min, max)
{4,} : atleast or more
'''

my_string = 'hello_123'
pattern = re.compile(r'\d*') #zero or more
matches = pattern.finditer(my_string)
for match in matches:
    print(match)
print()

pattern = re.compile(r'\d+') #one or more
matches = pattern.finditer(my_string)
for match in matches:
    print(match)
print()

my_string = 'hello_1_2-3'
pattern = re.compile(r'_?\d') #either there or not
matches = pattern.finditer(my_string)
for match in matches:
    print(match)
print()

my_string = '2020-04-01'
pattern = re.compile(r'\d{3}') # or if you need a range r'\d{3,5}'
matches = pattern.finditer(my_string)
for match in matches:
    print(match)
print()

my_string = '2020-04-01'
pattern = re.compile(r'\d{4,}') 
matches = pattern.finditer(my_string)
for match in matches:
    print(match)
print()

dates = '''
2020.04.01

2020-04-01
2020-05-23
2020-06-11
2020-07-11
2020-08-11

2020/04/02

2020_04_04
2020_04_04
'''
pattern = re.compile(r'\d{4}.\d{2}.\d{2}')
matches = pattern.finditer(dates)
for match in matches:
    print(match)
print()

pattern = re.compile(r'\d+.\d+.\d+')
matches = pattern.finditer(dates)
for match in matches:
    print(match)


pattern = re.compile(r'\d+[-\]\d+[-\]\d+')
matches = pattern.finditer(dates)
for match in matches:
    print(match)

my_string = '''
Mr Simpson
Mrs Simpson
Mr. Brown
Ms Smith
Mr. T'''

pattern = re.compile(r'Mr\.?\s\w+')
matches = pattern.finditer(my_string)
for match in matches:
    print(match)

print()
pattern = re.compile(r'(Mr|Ms|Mrs)\.?\s\w+')
matches = pattern.finditer(my_string)
for match in matches:
    print(match)