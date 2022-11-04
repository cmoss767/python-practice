course = "Python for beginners"
print(course.upper())
# find the index of the char y
# returns -1 if not found
print(course.find('y'))
# replaces for with 4
# strings are immutable so this results in a new string in memory
print(course.replace('for', '4'))

# checking to see if python is in course
# see a boolean value instead of index
print('Python' in course)
