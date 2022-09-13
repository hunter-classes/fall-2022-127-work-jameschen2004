# Fall 2022 - 127 - Work
# Name: James Chen

# GitHub username: jameschen2004

# this is my solution to exercises 7.7, 7.8, 7.10, 7.11 and Codingbat

#7.7
def is_even(n):
 print (n % 2 == 0)
is_even(int(input("Enter a number. ")))

#7.8
def is_odd(n):
  print (n % 2 != 0)
is_odd(int(input("Enter a number. ")))

#7.10
def is_right_angled(s1,s2,s3):
  print (abs(s3^2 - (s1^2 + s2^2)) <= .001) 
  
is_right_angled(3,4,5)

#7.11
def is_right_angledv2(s1,s2,s3):
  if s1 > s2 and s1 > s3:
        print (abs(s2**2 + s3**2 - s1**2) < 0.001)
  elif s2 > s1 and s2 > s3:
        print (abs(s1**2 + s3**2 - s2**2) < 0.001)
  else:
        print (abs(s1**2 + s2**2 - s3**2) < 0.001)
is_right_angledv2(3,6,9)

#Codingbat
def hello_name(name):
  return "Hello " + name + "!"

def make_out_word(out, word):
  return out[0:2] + word + out[2:len(str(out))]

def first_two(str):
  return str[0:2]
