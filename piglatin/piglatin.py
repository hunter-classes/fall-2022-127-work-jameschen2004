# Fall 2022 - 127 - Work
# Name: James Chen

# GitHub username: jameschen2004

# this is my solution to the bondify function and piglatin function

def bondify(name):
  first = name[0]
  first = first.upper()
  space = name.find(" ")
  last = name[space+1]
  last = last.upper()
  return(last + name[space+2:len(name)]+", "+ first + name[1:space] + " "+ last + name[space+2:len(name)])

print(bondify("james bond"))

def piglatin(name):
   if name[0].lower() == "a" or name[0].lower() == "e" or name[0].lower() == "i" or name[0].lower() == "o" or name[0].lower() == "u":
     return name.lower() + "yay"
   else:
     return name[1:99] + name[0:1].lower() + "ay"

print(piglatin("bapple"))


