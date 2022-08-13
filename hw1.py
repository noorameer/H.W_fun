# Create  a python file contains a group of function dealing with the "list"
# The group of function will be as follow:
# Function to find the biggest value in the list
# Function to find the summation of the list
# Function to find the average of the list
# Function to find the lowest value in the list
# ... Taking into account all the rules of the function...

def biggest(numlist):
    '''
    Function to find the biggest value in the list
    '''
    biggest_value = numlist[0]
    for i in numlist:
        if i > biggest_value:
            biggest_value = i

    print("the biggest_value is =", biggest_value)


def summation(list1):
    '''
    Function to find the summation of the list
    '''
    sum = 0
    for i in list:
        sum += i
    return sum


def average(len, sum):
    '''  
    Function to find the average of the list
    '''
    avg = sum/len
    print("avg =", avg)


def lowest(list3):
    '''
    Function to find the lowest value in the list
    '''
    low = list3[0]
    for i in list3:
        if i < low:
            low = i
    print("the lowest value is =", low)


list = [4, 7, 98, 25, 789, 187, 67, 3, 998, 742]
biggest(list)
sum = summation(list)
print("sum =", sum)
len_list = len(list)
average(len_list, sum)
lowest(list)
