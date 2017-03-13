print "You enter a dark room with two doors. Do you go throught door #1 OR door #2"

door = raw_input(">>")

if door == "1":
    print "There's a giant bear eating a cheesecake. What do you do?"
    print "1. Take the cake"
    print "2. Scream at the bear"

    bear = raw_input(">>")

    if bear == "1":
        print "The bear eats off your face. Good Job!!"
    elif bear == "2":
        print "Bear eats your leg off. Good Job!!"
    else:
        print "Well, doing %s is probably better. Bear runs away."%bear

elif door == "2":
    print "You stare into the endless abyss at Cthulhu's retina."
    print "1. Blueberries."
    print "2. Yellow jacket clothespins."
    print "3. Understanding revolvers yelling melodies."

    insanity = raw_input(">>")

    if insanity == "1" or insanity == "2":
        print "Your body survives with a mind of Jello. Good Job!!"
    else:
        print "The insanity rots your eyes into a pool of muck. Good Job again!!"

else:
        print "You stumble around and fall on a knife and die. Good Job!!"
