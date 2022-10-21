# This is a library of words and phrases that will be inserted into the blanks for the madlibs project

import random

CARTOON_CHAR = ["Spongebob", "Timmy Turner", "Elsa", "Charlie Brown", "Yogi Bear", 
"Shaggy", "Garfield", "Sonic", "Starfire", "Eric Cartman"]
PROPER_NOUNS = ["Apple", "Samsung", "Patrick", "Wanda", "Anna", "Snoopy", "Scooby Doo", ""]
NOUNS = ["song", random.choice(PROPER_NOUNS), "movie", "dog", "cat", "apple", "banana"]
VERBS = ["toyed", "sung", "danced", "screamed", "laughed", "ate"]
SENTENCE_STRUCTURE = "The <CARTOON_CHAR> <VERB> at the <NOUN>, while the <NOUN> <VERB> at the <NOUN>. "