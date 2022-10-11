#FUNCTIONS
# Max number
from operator import truediv


def max_num (num1, num2, num3):
    return max([num1, num2, num3])

# Multiply the list 
def mult_list(lst):
    if len(lst) == 0:
        return 0
    
    product = lst[0]

    if len(lst) > 1:
        for i in lst[1:]:
            product = product * i
    return product

# Reverse a string
def rev_string (str):
    return str[::-1]

# Number falls in range?
def num_within(a, b, c):
    #"b" is the initial value and "c" is the limit. The range operator syntax (start, stop, step) step is by how much the number is iterated by (set = 1 by default)
    num_range = range(b, c)

    if a in num_range:
        return True
    else:
        return False

#Pascal's Triangle
triangle = [[1], [1,1]]
def pascal(num):
    if num < 1:
        print('invalid number of rows')
    elif num == 1:
        print(triangle[0])
    else:
        row_number = 2
        while len(triangle) < num:
            row = []
            row_prev = triangle[row_number - 1]
            length = len(row_prev)+1
            for i in range(length):
                if i == 0:
                    row.append(1)
                elif i > 0 and i < length-1:
                    row.append(triangle[row_number - 1][i-1]+triangle[row_number - 1][i])
                else:
                    row.append(1)
                    triangle.append(row)    
                    row_number += 1
        for row in triangle:
            print(row)

#prints
print(max_num(100,300,5))
print(max_num(21500,30,5000))

print(mult_list([152,26,30]))
print(mult_list([1,2,3]))

print(rev_string('hello world'))
print(rev_string('python'))

print(num_within(1,2,3))
print(num_within(10,2,30))

pascal(5)
pascal(10)