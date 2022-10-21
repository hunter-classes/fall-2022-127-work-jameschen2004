'''
- Instead of specifying the sentences or story to convert, write a
  story in a file and read it from your program. Make sure to include
  the file in your repo and that your program reads it correctly.

- Add some replacements that are unique, that is, the first time you
  see them you select on randomly but then you keep reusing that
  replacement.

- Pay attention to letter case. That is, if you replace a word at the
  beginning of a sentence, it should be capitalized, otherwise,
  lowercase. This is except in the case of proper nouns which should
  always be capitalized. 
  '''
import random
CARTOON_CHAR = ["Spongebob", "Timmy Turner", "Elsa", "Charlie Brown", "Yogi Bear", 
"Shaggy", "Garfield", "Sonic", "Starfire", "Eric Cartman"]
PROPER_NOUNS = ["Apple", "Samsung", "Patrick", "Wanda", "Anna", "Snoopy", "Scooby Doo"]
NOUNS = ["song", "movie", "dog", "cat", "orange", "banana", random.choice(PROPER_NOUNS)]
VERBS = ["toyed", "sung", "danced", "screamed", "laughed", "ate", "cried"]

f = open("story.txt")
sentence = f.read

print(sentence)
CARTOON_CHAR = random.choice(CARTOON_CHAR)




#final_sentence = sentence_structure.join()