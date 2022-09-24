# Fall 2022 - 127 - Work
# Name: James Chen

# GitHub username: jameschen2004

# this is my solution to the bondify function and updated piglatin function

def bondify(name):
  first = name[0]
  first = first.upper()
  space = name.find(" ")
  last = name[space+1]
  last = last.upper()
  return(last + name[space+2:len(name)]+", "+ first + name[1:space] + " "+ last + name[space+2:len(name)])

print(bondify("james bond"))

def piglatin(name):
  if name[0] in 'AEIOUaeiou':
     if name[-1] in ".!?,":
       return name[0:int(len(name))-1] + "yay" + name[-1]
     else: 
       return name + "yay"
  else:
     if name[0] == name[0].lower():
       if name[-1] in ".!?,":
         return name[1:int(len(name))-1] + name[0] + "ay" + name[-1]
       else: 
         return name[1:] + name[0] + "ay"
     else:
       if name[-1] in ".!?,":
         return name[1].upper() + name[2:int(len(name))-1] + name[0].lower() + "ay" + name[-1]
       else:
         return name[1].upper() + name[2:] + name[0].lower()        + "ay"

print(piglatin("Bapple!"))


