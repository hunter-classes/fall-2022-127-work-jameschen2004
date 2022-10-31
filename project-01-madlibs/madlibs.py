'''
- Instead of specifying the sentences or story to convert, write a
  story in a file and read it from your program. Make sure to include
  the file in your repo and that your program reads it correctly. (story.txt)

- Add some replacements that are unique, that is, the first time you
  see them you select on randomly but then you keep reusing that
  replacement. (CARTOON_CHAR)

- Pay attention to letter case. That is, if you replace a word at the
  beginning of a sentence, it should be capitalized, otherwise,
  lowercase. This is except in the case of proper nouns which should
  always be capitalized. (period function)
  '''
from operator import index
import random
CARTOON_CHARS = ["Spongebob", "Timmy Turner", "Elsa", "Charlie Brown", "Yogi Bear", 
"Shaggy", "Garfield", "Sonic", "Starfire", "Eric Cartman"]
PROPER_NOUNS = ["Apple", "Samsung", "Patrick", "Wanda", "Anna", "Snoopy", "Scooby Doo"]
NOUNS = ["song", "movie", "dog", "cat", "orange", "banana"]
VERBS = ["shouted", "sung", "danced", "screamed", "laughed", "ate", "cried"]

f = open("project-01-madlibs/story.txt")
sentence = f.read()
sentence = sentence.replace("<CARTOON_CHAR>", random.choice(CARTOON_CHARS))
sentence = sentence.split()
c = 0
for word in sentence:
  if "<NOUN>" in word:
    sentence[c] = random.choice(NOUNS)
  if "<NOUN>" in word and len(word) > 6:
    sentence[c] = random.choice(NOUNS) + word[6:]
  if "<VERB>" in word:
    sentence[c] = random.choice(VERBS)
  if "<PROPER_NOUN>" in word:
    sentence[c] = random.choice(PROPER_NOUNS)
  c+=1
a = ''

for period in sentence:
  if "." in period:
    if period == sentence[-1]:
      sentence = sentence
    else:
      d = sentence.index(period)
      sentence[0] = sentence[0].capitalize()
      sentence[d+1] = sentence[d+1].capitalize()
    
sentence = " ".join(sentence)
print(sentence)
#   if word.find('.') > 0:
#     print(word.find('.'))
#     sentence[a+1].capitalize()
#   a+=1
# sentence = " ".join(sentence)
# find period index = number, substring that period index + 1, end of the string, then repeat 
#print(sentence)
