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


## Learn more with Automate the Boring Stuff:
## https://automatetheboringstuff.com/chapter1/