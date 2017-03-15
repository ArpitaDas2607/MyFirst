# Example code in python

import sys
import random

while True:
    question = raw_input("Ask magic 8 ball a question:(press enter to quit)")

    answers = random.randint(1,8)

# This command will take you out of the code if you type nothing
    if question == "":
        sys.exit()

    if answers == 1:
        print "Yup yup yup!"

    if answers == 2:
        print "Yes, you are close to what i am thinking!!"

    if answers == 3:
        print "Yeah right! like that's ever gonna happen!!"

    if answers == 4:
        print "Yes, i think you need some sleep"

    if answers == 5:
        print "It's as likely as you being hit by a comet at this very moment"

    if answers == 6:
        print "Maybe, someday"

    if answers == 7:
        print "NO!- just a big fat NO!"

    if answers == 8:
        print "Hell Yes!!"
