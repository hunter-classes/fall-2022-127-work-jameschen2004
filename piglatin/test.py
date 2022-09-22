def piglatin(name):
  if name[0] in 'AEIOUaeiou':
     return name + "yay"
  else:
     if name[0] == name[0].lower():
       return name[1:] + name[0] + "ay"
     else:
       return name[1].upper() + name[2:] + name[0].lower()        + "ay"

print(piglatin("Day"))