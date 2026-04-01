'''Set
^ (caret) negates the expression.
- (dash) specifies a range if it is in between, otherwise the dash itself.

Examples:
- [arn] Returns a match where one of the specified characters (a, r, or n) are present
- [a-n] Returns a match for any lower case character, alphabetically between a and n
- [^arn] Returns a match for any character EXCEPT a, r, and n
- [0123] Returns a match where any of the specified digits (0, 1, 2, or 3) are present
- [0-9] Returns a match for any digit between 0 and 9
- [0-5][0-9] Returns a match for any two-digit numbers from 00 and 59
- [a-zA-Z] Returns a match for any character alphabetically between a and z, lower case OR upper case'''

import re

test_string = 'hello 123_'
pattern = re.compile(r'[a-z]')
matches = pattern.finditer(test_string)
for match in matches:
    print(match)

dates = '''
01.04.2020

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

print('all dates with a character in between')
pattern = re.compile(r'\d{4}.\d{2}.\d{2}') 
matches = pattern.finditer(dates)
for match in matches:
    print(match)
print()

print('only dates with - or . in between')
pattern = re.compile(r'\d\d\d\d[-.]\d\d[-.]\d\d') #  no escape for the . here in the set
matches = pattern.finditer(dates)
for match in matches:
    print(match)
print()

print('only dates with - or . in between in May or June')
pattern = re.compile(r'\d\d\d\d[-.]0[56][-.]\d\d')
matches = pattern.finditer(dates)
for match in matches:
    print(match)
print()

print('only dates with - or . in between in May, June, July')
pattern = re.compile(r'\d\d\d\d[-.]0[5-7][-.]\d\d') #  no \. for fullstop in the set
matches = pattern.finditer(dates)
for match in matches:
    print(match)

#grouping
emails = """
pythonengineer@gmail.com
Python-engineer@gmx.de
python-engineer123@my-domain.org
"""
#pattern = re.compile(r'[a-zA-Z1-9-]+@[a-zA-Z-]+\.[a-zA-Z]+') #not grouped
pattern = re.compile(r'([a-zA-Z1-9-]+)@([a-zA-Z-]+)\.([a-zA-Z]+)') #grouped by ()
matches = pattern.finditer(emails)
for match in matches:
    print(match) #match object
    print(match.group()) #whole match
    print(match.group(0)) #whole match
    print(match.group(1)) #first group
    print(match.group(2)) #second group
    print(match.group(3)) #third group


'''Compilation Flags

ASCII, A : Makes several escapes like \w, \b, \s and \d match only on ASCII characters with the respective property.
DOTALL, S : Make . match any character, including newlines.
IGNORECASE, I : Do case-insensitive matches.
LOCALE, L : Do a locale-aware match.
MULTILINE, M : Multi-line matching, affecting ^ and $.
VERBOSE, X (for ‘extended’) : Enable verbose REs, which can be organized more cleanly and understandably.
'''

my_string = "Hello World"
pattern = re.compile(r'world', re.IGNORECASE) # No match without I flag
matches = pattern.finditer(my_string)
for match in matches:
    print(match)

my_string = '''
hello
cool
Hello
'''
# line starts with ...
pattern = re.compile(r'^[a-z]', re.MULTILINE) # No match without M flag
matches = pattern.finditer(my_string)
for match in matches:
    print(match)