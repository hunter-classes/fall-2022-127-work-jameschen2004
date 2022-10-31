# Fall 2022 - 127 - Work
# Name: James Chen

# GitHub username: jameschen2004

# This file contains a findLargest(l) function and a freq(l,v) function

list1 = [1,2,3,4,60,58,4,6,5,9,7,7,4,3,2]

def findLargest(l):
    largest_num = l[0]
    for num in l:
        if num > largest_num:
            largest_num = num
    return largest_num

print(findLargest(list1))

def freq(l,v):
    freq_of_num = 0
    for num in l:
        if num == v:
            freq_of_num = freq_of_num + 1
    return freq_of_num

print(freq(list1,1))

def mode(l):
    tmode = l[0]
    for num in l:
        if (freq(l,num)) > freq(l,tmode):
            tmode = num
    return (tmode)

mode(list1)