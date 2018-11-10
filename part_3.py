# LISTS
# https://docs.python.org/3/tutorial/introduction.html#lists

# list slicing [start:end:stride]

weekdays = ['mon','tues','wed','thurs','fri']
weekdays[0]         # element 0
weekdays[0:3]       # elements 0, 1, 2
weekdays[:3]        # elements 0, 1, 2
weekdays[-1]        # last element

test = weekdays[3:]        # elements 3, 4

weekdays

weekdays[-2]        # last element (element 4)
weekdays[::2]       # every 2nd element (0, 2, 4)
weekdays[::-1]      # backwards (4, 3, 2, 1, 0)

days = weekdays + ['sat','sun']     # concatenate lists

# Let's look at it another way
days_list = ['mon','tues','wed','thurs','fri']
days_list.append('sat') # append individual elements to list
days_list.append('sun')

#########
# Exercise - Lists
#########

# How do I slice out 'wed'?
# How do I check the type of 'mon'?
# How do I slice out 'wed' through 'friday'?
# What are two ways to slice out 'fri'?
# What is the length of days and days_list?
# How do I reverse the order of days? (hint: google it)