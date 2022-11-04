age = 20
print(age)

# returns a range object
# need to iterate over to show the nums
nums = range(5)
# only shows the assignment
print(nums)


for num in nums:
    print(num)

# shows 5-9
newNums = range(5, 10)

# shows 5-9 with a stepper of 2
newNums = range(5, 10, 2)

# can also do this
for num in range(5):
    print(num)
