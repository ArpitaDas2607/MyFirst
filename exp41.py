import random
from urllib import urlopen
import sys

WORD_URL = "http://learncodethehardway.org/words.txt"
WORDS = []

PHRASES = {
"class %%%(%%%):":
"Make a class named %%% that is-a %%%.",
"class %%%(object):\n\tdef__init__(self,***)":
"class %%% has-a __init__ that takes self and *** as arguments ",
"*** = %%%()":
"Set *** to an instance of class %%%.",
"***.***(@@@)":
"From *** get the *** fuction, call it with parameters self and @@@",
"***.*** = '***'":
"From *** get the *** attribute and set it to '***'."
}

#This particular line will check that there are exactly 2 arguments
#in the command line, and that the 2nd arguments is english
if len(sys.argv) == 2 and sys.argv[1] == "english":
    PHRASE_FIRST = True
else:
    PHRASE_FIRST = False


# will take all the wors in this URL and put it in a List named WORDS
for word in urlopen(WORD_URL).readlines():
    WORDS.append(word.strip())

def convert(snippet,phrase):
    class_names = [w.capitalize() for w in
                   random.sample(WORDS,snippet.count("%%%"))]
    other_names = random.sample(WORDS,snippet.count("***"))
    results = []
    param_names = []

    for i in range(0,snippet.count("@@@")):
        param_count = random.randint(1,3)
        param_names.append(', '.join(random.sample(WORDS,param_count)))

    for sentence in snippet,phrase:
        result = sentence[:]

        for word in class_names:
            result = result.replace("%%%",word,1)

        for word in other_names:
            result = result.replace("***",word,1)

        for word in param_names:
            result = result.replace("@@@",word,1)

        results.append(result)

    return results

try:
    while True:
        snippets = PHRASES.keys()
        random.shuffle(snippets)

        for snippet in snippets:
            phrase = PHRASES[snippet]
            question,answer = convert(snippet, phrase)
            if PHRASE_FIRST:
                question,answer = answer,question

            print question

            raw_input(">")
            print "ANSWER: %s\n\n\n"%answer

except EOFError:
    print "\nBye"
