# importing copy module
import copy

# initializing list 1
li1 = [1, 2, [3, 5], 4]

# using deepcopy for deepcopy
li2 = copy.deepcopy(li1)
li2[2][0] = -3
li1.pop(0)
li2.append(1000)

print('li1: ', li1)
print('li2: ', li2)
