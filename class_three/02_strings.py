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


# EXERCISE: 
# 1) Extract the year, month, day from the time stamps
# 2) Save each year, month and date as year_1, month_1, day_1
# Hint: yyyy-MM-dd hh:mm:ss

time_stamp_1 = "2011-10-02 18:48:05"
time_stamp_2 = "1973-12-12 08:28:08"
time_stamp_3 = "1999-11-06 14:12:13"


# HOMEWORK
# Look up datetime.strptime on google to learn more about datetime parsing

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

# another example: split a string into a list of substrings separated by a delimiter
address = 'Toluca Lake, CA 91602'
address.split(',')        # returns ['Toluca Lake','CA','91602']
address.split()           # same thing


## Learn more with Automate the Boring Stuff:
## https://automatetheboringstuff.com/chapter1/