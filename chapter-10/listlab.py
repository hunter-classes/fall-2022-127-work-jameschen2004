# Fall 2022 - 127 - Work
# Name: James Chen

# GitHub username: jameschen2004
# these are my functions to the lab hw due 10/13


numberlist = [51,1,4,6,5,9,8]
numberlistv2 = [1,2,3,4,5,6,7]
wordlist = ["these", "are", "all", "random", "words"]
strlist = ["random word", "random letter", "capitalized Letter", "CAPITALIZED WORD!"]
randomlist = numberlist + wordlist + strlist
sam_list = ["Hello", "my", "name", "is", "sam", "I", "like", "ham."]

def fix_value_error(list):  
  newlist = []
  for x in list:
    try:
      newlist.append(int(x)) 
    except ValueError:
      continue
  return newlist

def smallest_num_in_list(list):
  newlist = fix_value_error(list)
  smallest_value = newlist[0]
  for K in newlist:
    if K < smallest_value:
      smallest_value = K
  return smallest_value

print(smallest_num_in_list(randomlist))

def smallest_value_in_list(list):
  smallest_value = list[0]
  for K in list:
    if K < smallest_value:
      smallest_value = K
  return smallest_value

print(smallest_value_in_list(numberlist))

def shortest_word_in_list(list):
  shortest_word = list[0]
  for K in list:
    if len(K) < len(shortest_word):
      shortest_word = K
  return shortest_word

print(shortest_word_in_list(wordlist))

def odd_nums_list(list):
    newlist = fix_value_error(list)
    newlistv2 = []
    for number in newlist:
        if number % 2 == 1:
            newlistv2.append(number)
    return newlistv2

print(odd_nums_list(randomlist))

def capitalize_all(word):
  return word.upper()

print(capitalize_all("supercalifragilisticexpialidocious"))

  
def capitalize_longer_word(word):
  final = []
  word_bank = word.split()
  for word in word_bank:
    if len(word) > 5:
      word = word.upper()
    final.append(word)
  sentence = " ".join(final)
  return sentence

print(capitalize_longer_word("In order to have a complete sentence, the sentence must have a minimum of three word types: a subject, a verb, and an object."))

def sqr_all_nums(numlist):
  final_list = []
  for num in numlist:
    num = num **2
    final_list.append(num)
  return final_list

print(sqr_all_nums(numberlist))

def add_both_lists_nums(l1,l2):
  n = 0
  final_list = []
  for num1 in l1:
    final_list.append(num1+l2[n])
    n = n + 1
  return final_list

print(add_both_lists_nums(numberlist,numberlistv2))

# chapter 10 # 10 11 12 answers

def five_letter_list(word_list):
  final_list = []
  for word in word_list:
   if len(word) == 5:
     final_list.append(word)
  return final_list

print(five_letter_list(wordlist))

def sum_all_nums_up_to_one_even(numlist):
  final_sum = 0
  for num in numlist:
    if num % 2 == 0:
      return final_sum
    else:
      final_sum = final_sum + num
      
      

print(sum_all_nums_up_to_one_even(numberlist))

def sam_stopper_counter(list):
  n = 0
  for item in list:
    n = n + 1
    if item == "sam":
      return n
print(sam_stopper_counter(sam_list))