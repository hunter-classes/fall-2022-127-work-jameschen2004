# Extras that I have done are

import madlib_library
import random

CARTOON_CHAR = random.choice(madlib_library.CARTOON_CHAR)
sentence_structure = madlib_library.SENTENCE_STRUCTURE.split()
def replace_nouns(sentence_structure):
    final_sentence_structure = []
    for noun in sentence_structure:
        if noun == "<NOUN>":
            final_sentence_structure.append(random.choice(madlib_library.NOUNS)) 
    return final_sentence_structure

print(replace_nouns(sentence_structure))
print(random.choice(madlib_library.NOUNS))
print(sentence_structure)