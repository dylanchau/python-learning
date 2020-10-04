# Example 01
import functools
import itertools

List = []
print('Blank List: ', end='')
print(List)

# List of numbers
List = [1, 2, 3, 10.5]
print('List of numbers: ', end='')
print(List)

# List of strings and accessing by index
List = ['I', 'Lover', 'You']
print('List of strings: ', end='')
print(List[0], end=' ')
print(List[1], end=' ')
print(List[2], end='\n')

# Multiple Dimensional list
List = [[1, 2, 3], ['A', 'B', 'c']]
print('Multiple-Dimensional List: ', end='')
print(List, end='\n')

# Size of List
List = []
print('Length of empty list: {0}'.format(len(List)))

List = [1, 2, 3]
print('Length of numbers list: {0}'.format(len(List)))

# Manipulate List

# append() to insert element to tail of a list
List = []
List.append('ABC')
print(List)

# add elements to list using append() with loop
List = []

for i in range(1, 6):
    List.append(i)

print(List)

# add a Tuple to an existing list
List.append((6, 7, 8, 9, 10))
print(List)

# insert(index, value) to add an element to a list with desire position (before index)
List.insert(5, 'ABC')
print(List)

# extend() add multiple elements at the same time
List.extend([10, 11, [15, 20]])
print(List)

print(List[0])
print(List[5])
print(List[6])
print(List[9])
print(List[9][0])
print(List[9][1])

print('Value at position -1: {0}'.format(List[-1]))

# remove() - function but an Error arises if element doesn’t exist in the set
# Note - Remove method in List will only remove the first occurrence of the searched element.

List = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
List.remove(1)
print(List)

# pop() - remove an element from a list. Default remove the last element,
# to remove element from a specific position index need to be past as an argument
# error will be raised if remove an empty list

List = [1, 2, 3]
List.pop()
List.pop()
List.pop()
print(List)


"""
 - - Default beginning of Seq 
|
|   0   1   2   3   4   5   6   7   8   9   10  
->  +++++++++++++++++++++++++++++++++++++++++
    + H + E + L + L + O + W + O + R + L + D + 
    +++++++++++++++++++++++++++++++++++++++++
   -10 -9  -8  -7  -6  -5  -4  -3  -2  -1   ^
                                        ^   |
                                        |   |
             string using [::-1] --------   |
                                        Default end of seq
"""

List = ['H', 'E', 'L', 'L', 'O', 'W', 'O', 'R', 'L', 'D']

# if end_index is out-of-range, the default end seq will be used
print(List[:5])
# if end_index is out-of-range, the default beginning seq will be used
print(List[:-5])
# if start_index is out-of-range, the default end seq will be used
print(List[5:])

print(List[5:10])

# Reverse list
print(List[::-1])

############### List Methods ###############

del List[5: 10]
print(List)

List.pop(-2)
print(List)

# Remove all occurrence of an item in list


def remove_items(test_list, item):
    # solution 1
    # res = [i for i in test_list if i != item]

    # solution 2
    res = list(filter((item).__ne__, test_list))

    return res


List = [1, 1, 2, 3, 4, 5, 1, 2]
print(f'Initial List {List}')

print('Remove all occurence of {0} in list and result: {1}'.format(
    1, str(remove_items(List, 1))))

# index(element, start, end) - search index of given <element> from start to end,
# and return lowest index where the element appears. Error raised if element not found.
print(f'Index of {5} in the list is {List.index(5)}')

# find all occurrences of an element in a list?
print('Index of all occurence of 1 in list and result: ',
      [i for i, x in enumerate(List) if x == 1])

# count(v) - returns count of how many times a given object occurs in list
print(f'The time occurence of 1 in the list is {List.count(1)}')

# To get the number of occurrences of each item in a list
print([[l, List.count(l)] for l in set(List)])

# To get the number of occurrences of each item in a dictionary
print(dict((l, List.count(l)) for l in set(List)))


# sort([reverse=True]) - sort function
List.sort(reverse=True)
print(List)

employee_list = [
    {'Name': 'Alan Turing', 'age': 25, 'salary': 10000},
    {'Name': 'Sharon Lin', 'age': 30, 'salary': 8000},
    {'Name': 'John Hopkins', 'age': 18, 'salary': 1000},
    {'Name': 'Mikhail Tal', 'age': 40, 'salary': 15000},
]


def get_name(employees):
    return employees.get('Name')


def get_salary(employees):
    return employees.get('salary')


# employee_list.sort(key=get_salary, reverse=True)
# using lambda function
employee_list.sort(key=lambda e: e.get('salary'), reverse=True)
print(employee_list)


# Built-in functions with List


# reduce(func, seq) - is used to apply a particular function passed in its argument
# to all of the list elements mentioned in the sequence passed along
lis = [1, 3, 5, 6, 2, ]
print("The sum of the list elements is : ", end="")
print(functools.reduce(lambda a, b: a + b, lis), end="\n\n")
print(
    f'itertools.accumulate: {list(itertools.accumulate(lis, lambda a, b: a + b))}')

print("The maximum element of the list is : ", end="")
print(functools.reduce(lambda a, b: a if a > b else b, lis))
