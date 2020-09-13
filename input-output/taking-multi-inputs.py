# Python program showing how to
# multiple input using split

# x, y = input('Enter a two values: ').split()
# print('Number of boys:', x)
# print('Number of girls:', y)
# print()

# taking three inputs at a time
# x, y, z = input('Enter a three values: ').split()
# print('Total number of students:', x)
# print('Number of boys:', y)
# print('Number of girls:', z)
# print()

# taking two inputs at a times
# a, b = input('Enter a two values: ').split()
# print('First number is {} and second number is {}'.format(a, b))

# taking multiple inputs at a time
# and type casting using list() function
# x = list(map(int, input('Enter a multile value: ').split()))
# print('List of students: ', x)

# Python program showing
# how to take multiple input
# using List comprehension
# taking multiple inputs at a time
x = [int(x) for x in input('Enter multiple value: ').split()]
print('Number of list:', x)
