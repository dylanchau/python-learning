# # python is dynamic type
# """ it does not need data type for a variable  """
# variable = 1
# print(variable)

# variable = 5.5
# print(variable)

# variable = "Hello World!!!"
# print(variable)

# variable = []
# variable.append('Hi')
# variable.append(100.50)
# print(variable)

# # take input from user
# name = input('What is your name:')
# print("Welcome:", name)

# # convert input data type
# num1 = int(input('a = '))
# num2 = int(input('b = '))
# print('a + b =', num1 + num2)

# # selection
# if (num1 > num2):
#     print('{} > {}'.format(num1, num2))
# elif(num1 < num2):
#     print('{} < {}'.format(num1, num2))
# else:
#     print('{} == {}'.format(num1, num2))

# # def function
# """
#   def function-name(arguments):
#             #function body
# """


# def sum(a, b):
#     return a + b


# print('{0:.2f}'.format(sum(num1, num2)))

# Main function

import math


def greeting():
    return 'Hello World!!!'


def Main():
    # print(greeting())

    # for i in range(11):
    #     print(math.fabs(i))
    print(True == 1)


if __name__ == "__main__":
    Main()
