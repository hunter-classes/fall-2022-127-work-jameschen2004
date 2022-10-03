# Fall 2022 - 127 - Work
# Name: James Chen

# GitHub username: jameschen2004

# this is my solution to chapter 10 exercises 5, 7 and 8

def max(numlist):
    greatest_value = numlist[0]
    for num in numlist:
        if greatest_value < num:
            greatest_value = num
    return greatest_value

print(max([1,21,3,4,5]))

def num_of_odd_nums(numlist):
    num = 0
    for number in numlist:
        if number % 2 == 1:
            num = num + 1
    return num

print(num_of_odd_nums([1,3,5,7,9,10]))

def sum_of_even_nums(numlist):
    sum = 0
    for num in numlist:
        if num % 2 == 0:
            sum = sum + num
    return sum

print(sum_of_even_nums([2,4,6,8,9]))
