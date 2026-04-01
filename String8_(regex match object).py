import re

'''
match(): Determine if the RE matches at the beginning of the string.
search(): Scan through a string, looking for any location where this RE matches.
findall(): Find all substrings where the RE matches, and returns them as a list.
finditer(): Find all substrings where the RE matches, and returns them as an iterator.'''

'''methods of match object
group(): Return the string matched by the RE
start(): Return the starting position of the match
end(): Return the ending position of the match
span(): Return a tuple containing the (start, end) positions of the match'''

# finditer()
my_string = 'abc123ABC123abc'
pattern = re.compile(r'123')
matches = pattern.finditer(my_string)
for match in matches:
    print(match)
    print(match.span(), match.start(), match.end())
    print(match.group(0)) # returns the string #group() or group(0) both same
print()
matches = re.finditer(r'abc', my_string)
for match in matches:
    print(match)
print()

# findall()
pattern = re.compile(r'123')
matches = pattern.findall(my_string)
for match in matches:
    print(match)
print(matches) #returns a list of matches
print()

# match
match = pattern.match(my_string) #only check if found at beginning
print(match) #if not return none
pattern = re.compile(r'abc')
match = pattern.match(my_string)
print(match)
print()

# search
match = pattern.search(my_string)
print(match) #check throughout return first found span
print()