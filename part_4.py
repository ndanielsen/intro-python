## FOR LOOPS

# print 0 through 5 on a separate line
nums = [0, 1, 3, 4, 5]

for num in nums:
    print(num)

# for loop to create a list of cubes
cubes = []
for num in nums:
    cubes.append(num**3)


##### CONDITIONALS ######

# We will use an if else to implement logic
x = 15
if x  > 10 :
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
else:   #implicity means else if temperature >=212
    print("water will boil")


#########
# EXERCISE For Loops
#########
# Given that: letters = ['a','b','c']
# Write a for-loop that returns: ['A','B','C']


# Given that: nums = [0, 1, 3, 4, 5]
# Write a for-loop that sums the total of all the numbers in the list


# Given that: nums = [0, 1, 3, 4, 5]
# Write a for-loop that prints out even numbers
