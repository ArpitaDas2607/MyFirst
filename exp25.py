def break_words(stuff):
    '''This function will, break up words for us.'''
    words = stuff.split(' ')
    return words

#Trial 1:
#print words
stuff = "Now this looks weird, it\'s blue and green and all in between"
statements = break_words(stuff)
print statements
#-----------------------------------------------------------------------------#
def sort_words(words):
    '''This will sort words'''
    return  sorted(words)

#Trial 2:
wordsNew = "Expeliarimus"
trial = sort_words(wordsNew)
print trial

#-----------------------------------------------------------------------------#

def print_first_word(words):
    '''Prints the first word after popping it off'''
    word = words.pop(0)
    return word

#Trial 3:
#Note that an argument for pop is always a list which can be created from a sentence by split(' ')
#aList = [123, 'xyz','zara','abc']
print statements
firstWord = print_first_word(statements)
print firstWord

#-----------------------------------------------------------------------------#

def print_last_word(words):
    '''Prints last word after popping it off'''
    word = words.pop(-1)
    print word

#Trial 4:
print statements
LastWord = print_last_word(statements)
print LastWord

#-----------------------------------------------------------------------------#

def sort_sentence(sentence):
    '''Takes in a full sentence and returns the sorted words'''
    words = break_words(sentence)
    return sort_words(words)

#Trial 5:
Break = sort_sentence("I am Das")
print Break

#-----------------------------------------------------------------------------#

def print_first_and_last(sentence):
    '''Prints the first and last words of the sentence'''
    words = break_words(sentence)
    a = print_first_word(words)
    b = print_last_word(words)
    return a,b

#Trial 6:
A,B = print_first_and_last("I am Das too")
print A
print B

#-----------------------------------------------------------------------------#

def print_first_and_last_sorted(sentence):
    '''Sorts the words then prints the first and last one '''
    words = sort_sentence(sentence)
    a = print_first_word(words)
    b = print_last_word(words)

#Trial 7:
A,B = print_first_and_last("I am Das as well")
print A
print B
