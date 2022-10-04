def piglatin(name):
   first = name.lower()
   first = name[0]
   print(first)
   if first != "a" or "e" or "i" or "o" or "u":
      return name[1:len(name)] + name[0] + "ay"
   if first == "a" or "e" or "i" or "o" or "u":
      return name + "yay"

print(piglatin("apple"))
