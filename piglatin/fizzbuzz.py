def fizzbuzz(n):
  i = 0
  while i < n:
     i = i + 1
     if i % 3 == 0 and i % 5 == 0:
       print("fizzbuzz")
     elif i % 3 == 0:
       print("fizz")
     elif i % 5 == 0:
       print("buzz")
     else:
       print(i)

fizzbuzz(100)