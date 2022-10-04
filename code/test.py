def initialize(name):
  first = name[0]
  first = first.upper()
  space = name.find(" ")
  last = name[space+1]
  last = last.upper()
  return(first + ". " + last + name[space+2:len(name)])

print(initialize("james bond"))

def bondify(name):
  first = name[0]
  first = first.upper()
  space = name.find(" ")
  last = name[space+1]
  last = last.upper()
  return(last + name[space+2:len(name)]+", "+ first + name[1:space] + " "+ last + name[space+2:len(name)])

print(bondify("james bond"))
def is_even(n):
  return(n%2 == 0)
print(is_even(10))

def is_odd(n):
  return not is_even(n)

print(is_odd(11))
