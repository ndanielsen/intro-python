## DICTIONARIES

# dictionaries are similar to lists:
# - both can contain multiple data types
# - both are iterable
# - both are mutable

# dictionaries are different from lists:
# - dictionaries are unordered*
# - dictionary lookup time is constant regardless of dictionary size

# dictionaries are like real dictionaries:
# - dictionaries are made of key-value pairs (word and definition)
# - dictionary keys must be unique (each word is only defined once)
# - you can use the key to look up the value, but not the other way around

# Create a dictionary
family = {'dad':'homer', 'mom':'marge', 'size':6}

# Xxamine a dictionary
# family[0]           # throws an error (there is no ordering)
family['dad']       # returns 'homer'
len(family)         # returns 3
family.keys()       # returns list: ['dad', 'mom', 'size']
family.values()     # returns list: ['homer', 'marge', 6]
family.items()      # returns list of tuples:
                    #   [('dad', 'homer'), ('mom', 'marge'), ('size', 6)]

# Modify a dictionary
family['cat'] = 'snowball'          # add a new entry
family['cat'] = 'snowball ii'       # edit an existing entry
del family['cat']                   # delete an entry
family['kids'] = ['bart', 'lisa']   # value can be a list

# accessing a list element within a dictionary
family['kids'][0]   # returns 'bart'

# Check if an address is present
family.get('address')

# Addition operations on a key
family['size'] = family['size'] + 1
# ---- or ----
family['size'] += 1

# EXERCISE:
# Given that: d = {'a':10, 'b':20, 'c':[30, 40]}

# First, print the value for 'a'

# Then, change the value for 'b' to be 25

# Then, change the 30 to be 35

# Finally, append 45 to the end of the list that contains 35 and 40
