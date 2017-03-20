#This code is the first quiz game i am creating on my own

import sys
import random


def final_door():
    question =random.randint(1,5)
    global count
    count = 10


    if question == 1:
        print "\n\n\tPeso is the currency of which country?\n\n"
    if question == 2:
        print "\n\n\tWhat is the capital of Fiji?\n\n"
    if question == 3:
        print "\n\n\tIn which month is Christmas celebrated?\n\n"
    if question == 4:
        print "\n\n\tWhat is the capital of Switzerland?\n\n"
    if question == 5:
        print "\n\n\tWhich is the smallest country in the world?\n\n"

    answer = raw_input(">>>").lower()

    if question == 1 and answer == "argentina":
        print "Well done! You are a step closer to the finishing line!!"
        count = count + 30
    elif question == 2 and answer == "suva":
        count = count + 30
        print "Well done! You are a step closer to the finishing line with %d coins in your pocket!!"%count
    elif question == 3 and answer == "december":
        count = count + 30
        print "Well done! You are a step closer to the finishing line with %d coins in your pocket!!"%count
    elif question == 4 and answer == "bern":
        count = count + 30
        print "Well done! You are a step closer to the finishing line with %d coins in your pocket!!"%count
    elif question == 5 and answer == "vatican":
        count = count + 30
        print "Well done! You are a step closer to the finishing line with %d coins in your pocket!!"%count

    else:
        print "\a\a\aOops! You just died!"
        sys.exit()

    print "\aNow you will play for your life and 50 more coins"
    question1 = random.randint(1,5)

    if question1 == 1:
        print "\n\n\tYen is the currency of which country?\n\n"
    if question1 == 2:
        print "\n\n\tWhat is the capital of China?\n\n"
    if question1 == 3:
        print "\n\n\tIn which month is Easter celebrated?\n\n"
    if question1 == 4:
        print "\n\n\tWhat is the capital of New Zealand?\n\n"
    if question1 == 5:
        print "\n\n\tWhich is the largest country in the world?\n\n"

    answer1 = raw_input(">>>").lower()

    if question1 == 1 and answer1 == "japan":
        print "Well done! You are a step closer to the finishing line!!"
        count = count + 50
    elif question1 == 2 and answer1 == "beijing":
        count = count + 50
        print "Well done! You are a step closer to the finishing line with %d coins in your pocket!!"%count
    elif question1 == 3 and answer1 == "april":
        count = count + 50
        print "Well done! You are a step closer to the finishing line with %d coins in your pocket!!"%count
    elif question1 == 4 and answer1 == "auckland":
        count = count + 50
        print "Well done! You are a step closer to the finishing line with %d coins in your pocket!!"%count
    elif question1 == 5 and answer1 == "russia":
        count = count + 50
        print "Well done! You are a step closer to the finishing line with %d coins in your pocket!!"%count

    else:
        print "\a\a\aOops! You just died!"
        sys.exit()

    print "\aNow you will play to win 100 more coins"
    question2 = random.randint(1,5)

    if question2 == 1:
        print "\n\n\tWhich movie did karishma kapoor win a national award for?\n\n"
    if question2 == 2:
        print "\n\n\tWhat is the colour between blue and green called?\n\n"
    if question2 == 3:
        print "\n\n\tWhat are moving stairs called?\n\n"
    if question2 == 4:
        print "\n\n\In which state was gandiji born?\n\n"
    if question2 == 5:
        print "\n\n\tWho was the first president of India?\n\n"

    answer2 = raw_input(">>>").lower()

    if question2 == 1 and answer2 == "zubeida":
        print "Well done! You have crossed the finish line!!"
        count = count + 100
    elif question2 == 2 and answer2 == "turquoise":
        count = count + 100
        print "Well done! You have crossed the finish line with %d coins in your pocket!!"%count
    elif question2 == 3 and answer2 == "escalator":
        count = count + 100
        print "Well done! You have crossed the finish line with %d coins in your pocket!!"%count
    elif question2 == 4 and answer2 == "porbandar":
        count = count + 100
        print "Well done! You have crossed the finish line with %d coins in your pocket!!"%count
    elif question2 == 5 and answer2 == "dr. rajendra prasad":
        count = count + 100
        print "Well done! You have crossed the finish line with %d coins in your pocket!!"%count

    else:
        print "\a\a\aOops! You just died!"
        sys.exit()

    return count




print """\tYou have now overcome the penultimate door,
\tanswer the following questions if you want to stay alive"""

final_door()
