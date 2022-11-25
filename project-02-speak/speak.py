"""
Extras done: 4
- Store your translations in a file named pirate.dat 
The file should have lines in the form “word:translation."

- Handle upper and lower case and/or punctuation

- Have an option to translate different languages.

- Try to tackle more advanced translations like converting parts of
words rather than straight substitutions or inserting pirate phrases
at appropriate points in your document.
"""
import re
pirate_dict = {}
unshakespearify_dict = {}
story_file = open("input.txt")
capitalize_nouns = ["blackbeard","romeo","Romeo","i'll","montague","capulet"]
punctuation = [".",",","?","!"]

with open("pirate.dat") as file:
  for line in file:
    (key,value) = line.split(":")
    pirate_dict[(key)] = value.strip()

with open("unshakespearify.dat") as file:
  for line in file:
    (key,value) = line.split(":")
    unshakespearify_dict[(key)] = value.strip()
story = []
story2 = []
storyline = story_file.read().split()
storyline2 = storyline
for word in storyline:
  include = False
  if word[-1] in punctuation:
    for key in pirate_dict.keys():
      if key == word[:-1]:
        include = True
        story.append(pirate_dict[key] + word[-1])
    if include == False:
      story.append(word)
  else:
    if word in pirate_dict.keys():
      for key in pirate_dict.keys():
        if key in word:
          story.append(pirate_dict[key])
    else:
      story.append(word)
story = " ".join(story)
for definition in pirate_dict.keys():
  if " " in definition:
    story = story.replace(definition,pirate_dict.get(definition))

story = story.lower()
rtn = re.split('([.!?:] *)', story)
story = ''.join([i.capitalize() for i in rtn])
for word in capitalize_nouns:
  story = story.replace(word,word.capitalize())

for word in storyline2:
  include = False
  if word[-1] in punctuation:
    for key in unshakespearify_dict.keys():
      if key == word[:-2]:
        include = True
        story2.append(unshakespearify_dict[key] + word[-1])
    if include == False:
      story2.append(word)
  else:
    if word in unshakespearify_dict.keys():
      for key in unshakespearify_dict.keys():
        if key in word:
          story2.append(unshakespearify_dict[key])
    else:
      story2.append(word)
story2 = " ".join(story2)
story2 = story2.lower()

rtn = re.split('([.!?:] *)', story2)
story2 = ''.join([i.capitalize() for i in rtn])
for word in capitalize_nouns:
  story2 = story2.replace(word,word.capitalize())

for definition in unshakespearify_dict.keys():
  if " " in definition:
    story2 = story2.replace(definition,unshakespearify_dict.get(definition))
print("Pirate Speak: \n" + story)

x = input("Would you like to read the unshakespearified version? \n")
if x in ["Yes","yes","Y","y"]:
  print("Unshakespearified Speak: \n" + story2)