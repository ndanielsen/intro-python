## FOR LOOPS

# print 0 through 5 on a separate line
nums = [0, 1, 3, 4, 5]

for num in nums:
    print(num)

# for loop to create a list of cubes
cubes = []
for num in nums:
    cubes.append(num ** 3)


##### CONDITIONALS ######

# We will use an if else to implement logic
x = 15
if x > 10:
    print("x is more than 10!")
    print("hooray")
elif x > 100:
    print("x is HUGE")

# As soon as one conditional is satisfied, it stops checking!

temperature = 20
if temperature <= 32:
    print("water is ice")
elif temperature > 32 and temperature < 212:
    print("water is liquid")
else:  # implicity means else if temperature >=212
    print("water will boil")


## LIST COMPREHENSIONS WITH CONDITIONS
# range when passed to a list, produces a range of numbers

nums = list(range(1, 6))

# for loop to create a list of cubes of even numbers
cubes_of_even = []
for num in nums:
    if num % 2 == 0:
        cubes_of_even.append(num ** 3)

# equivalent list comprehension
# syntax: [expression for variable in iterable if condition]

cubes_of_even = [num ** 3 for num in nums if num % 2 == 0]  # [8, 64]


#########
# EXERCISE For Loops
#########
# Given that: letters = ['a','b','c']
# Write a for-loop that returns: ['A','B','C']


# Given that: nums = [0, 1, 3, 4, 5]
# Write a for-loop that sums the total of all the numbers in the list


# Given that: array = [{"num": 1}, {"num": 4}, {"num" : 7}]
# Write a for-loop that prints out even numbers

