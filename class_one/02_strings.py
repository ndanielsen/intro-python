# STRINGS
# https://docs.python.org/3/tutorial/introduction.html#strings

s = str(42)

s  # convert another data type into a string (casting)

s = 'I like you'

# examine a string
s[0]  # returns 'I'

len(s)  # returns 10

# string slicing like lists
s[0:7]  # returns 'I like '

s[6:]  # returns 'you'

s[-1]  # returns 'u'

# Use the 'repr()'
# repr() is string representation
repr(s[0:7])

# EXERCISE: Book Titles (Part 1)
# 1) Extract the book title from the string
# 2) Save each book title to a variable (ie book1_title)
# 3) How many characters/elements are in each title?
# Hint: {bookTitle} by {author}, {years}


book1 = "Beyond the Door by Dick, Philip K., 1928-1982"
book2 = "The Variable Man by Dick, Philip K., 1928-1982"
book3 = "The Skull by Dick, Philip K., 1928-1982"


# STRINGS - Part II

# concatenate strings
s3 = 'The meaning of life is'
s4 = '42'
s3 + ' ' + s4       # returns 'The meaning of life is 42'
s3 + ' ' + str(42)  # same thing

# split a string into a list of substrings separated by a delimiter

s = 'I like you'
s.split(' ')        # returns ['I','like','you']
s.split()           # same thing

# Reverse a string

string = 'Hello, my friend!' 

string[::-1]

# Replace substring with another value

cheese_str = 'I like yummy cheese'

cheese_str.replace('like', 'love')


# BONUS EXERCISE - 	Palindrome Detection
# A palindrome is a word, phrase, number or sequence of words that 
# reads the same backwards as forwards. 
# Punctuation and spaces between the words or lettering is allowed. 

# 1) Can you programmatically test if these phrases are palindromes?

palindrome_one = 'racecar'


palindrome_two = 'step on no pets' 


palindrome_three = 'Red rum, sir, is murder!' 

# hint - how can you lowercase a string?
# hint - how can you remove / replace punctuation with an empty string?
# Next level exercise - see 03_functions.py

## Learn more with Automate the Boring Stuff:
## https://automatetheboringstuff.com/chapter1/