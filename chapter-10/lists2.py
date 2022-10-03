# Fall 2022 - 127 - Work
# Name: James Chen

# GitHub username: jameschen2004

# this is my solution to chapter 10 exercises 4 and 6

def average(pos):
    total = 0
    for num in pos:
        total = total + num
        ans = total / len(pos)
    return ans
print(average([1,3,5]))

def sum_of_squares(xs):
    total = 0
    for num in xs:
        num = num ** 2
        total = num + total
    return total
print(sum_of_squares([4,2,3]))
