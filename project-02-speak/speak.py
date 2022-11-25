"""
Extras done: 4
- Store your translations in a file named pirate.dat 
The file should have lines in the form “word:translation."

- Handle upper and lower case and/or punctuation

- Have an option to translate different languages.

-  Try to tackle more advanced translations like converting parts of
words rather than straight substitutions or inserting pirate phrases
at appropriate points in your document.
"""

pirate_dict = {}
unshakespearify_dict = {}
story_file = open("input.txt")
story2 = story_file

proper_nouns = ["Jack Sparrow","Montague"]
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
storyline = story_file.read().split()
for word in storyline:
  include = False
  if word[-1] in punctuation:
    for key in pirate_dict.keys():
      if key in word:
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
  story = story.replace(definition,pirate_dict.get(definition))

print(story2)
for definition in unshakespearify_dict.keys():
  story2 = story2.replace(definition,unshakespearify_dict.get(definition))
print("Pirate Speak: \n" + story)

