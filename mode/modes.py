# Fall 2022 - 127 - Work
# Name: James Chen

# GitHub username: jameschen2004

# This file contains a findLargest(l) function and a freq(l,v) function
# Fast mode was added to this file

list1 = [1,2,3,4,60,58,4,6,5,9,7,7,4,3,2]

def findlargest(l):
    largest_num = l[0]
    for num in l:
        if num > largest_num:
            largest_num = num
    return largest_num

print(findlargest(list1))

def freqv1(l,v):
    freq_of_num = 0
    for num in l:
        if num == v:
            freq_of_num = freq_of_num + 1
    return freq_of_num

print(freqv1(list1,4))
import datetime
from gettext import find
import random

def findLargest(dataset):
    largeSoFar = dataset[0]
    for item in dataset[1:]:
        if item > largeSoFar:
            largeSoFar = item
    return largeSoFar



def freq(dataset,v):
    # since this loops over the
    # entire data set once
    # it takes n time 
    #count = 0
    #for item in dataset:
    #    if item == v:
    #        count = count + 1
    #return count
    return len([x for x in dataset if x == v])

def buildRandomList(size,maxvalue):
    #result = []
    #for x in range(size):
    #    result.append(random.randrange(maxvalue))
    #return result
    result = [random.randrange(maxvalue) for x in range(size)]
    return result 


def mode(dataset):
    """
    Returns a mode of the dataset, that is
    the value that appears most frequently

    if multiple values appear the same # of times and are
    most frequent, return any of them.

    Ex: mode([5,4,5,6,7,8,5,4]) --> 5 since 5 appears the most
    mode([5,5,5,4,4,4,2,2,7,7,8,8,9]) --> return 5 or 4 since
    both of those values appear 3 times which is the most

    Strategy:
    assume the first value is the mode
    we can grab its frequency

    for each remaining item in the dataset:
      count that items frequence and see if it's the new
      mode so far    
    """
    modeSoFar = dataset[0]
    freqSoFar = dataset.count(modeSoFar)
    for item in dataset[1:]: #outer loop -> n
        # calling freq each time is n
        # if freq(dataset,item) > freqSoFar:
        if dataset.count(item) > freqSoFar:
            modeSoFar = item
            freqSoFar = dataset.count(item)
    return modeSoFar


def fastMode(dataset):
    # assume all values in dataset
    # are between 0 and 99 inclusive
    print("Dataset Size:   99")
    # 1. make a list of 100 slots
    # and set them all to 0
    # this will store our tallies
    
    tally_list = []
    for i in range(100):
        tally_list.append(0)
    # 2. Loop through our dataset
    # and for each item incremement
    # (add 1) to the appropriate
    # slot in the tallies list
    for item in dataset:
        tally_list[item] = tally_list[item] + 1
    # 3. the index with the highest
    # value in tallies is the mode
    return tally_list.index(findLargest(tally_list))
    pass

    
def testMode(size,maxValue):
    print("Dataset Size: ",size)
    dataset = buildRandomList(size,maxValue)
    # print(dataset)
    m = mode(dataset)
    print("Mode: ",m)

def testFindLargest(size,maxValue):
    print("Dataset Size: ",size)
    dataset = buildRandomList(size,maxValue)
    # print(dataset)
    m = findLargest(dataset)
    print("Largest: ",m)

#testFindLargest(80000,30)
dataset = buildRandomList(100,99)
print(fastMode(dataset))

