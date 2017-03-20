from sys import exit



def bear_room():
    print "There is a bear in here."
    print "The bear has a bunch of honey"
    print "The fat bear is in front of another door"
    print "How are you going to mmove the bear?"
    bear_moved = False

    while True:
        choice = raw_input(">>")

    if choice == "Take Honey":
            dead("The bear looks at you and slaps your face off.")
    elif choice == "Taunt bear" and not bear_moved:
            print "The bear has moved from the door. You can go through and find redemption"
#we are now changing the value of bear_moved, but why so? which one of these values will be considered?

            bear_moved = True
    elif choice == "Taunt bear" and bear_moved:
            dead("The bear gets pissed and chews off your entire leg off")
    elif choice == "open door" and bear_moved:
            gold_room()
    else:
            print "I got no idea what that means"


def gold_room():
    print "This room is full of gold.How much do you take?????"

    choice = raw_input(">>")
    if "0" in choice or "1" in choice:
        how_much = int(choice)
    else:
        dead("Man,learn to type a number.")

    if how_much<50:
        print "Nice, you are not greedy, you win!"
    else:
        dead("You are a greaady dumbo!")



def cthulhu_room():
    print '''\tHere you see the great evil Cthulhu,
    He, it, whatever it is stares at you and you go insane.
    Do you flee for your life or eat your head?'''

    choice = raw_input(">>")

    if "flee" in choice:
        start()
    elif "head" in choice:
        dead("Well, that was tasty")
    else:
        cthulhu_room()

def dead(why):
        print why,"Good Job!"
        exit(0)

def start():
        print '''\tYou are in a dark room.
        There is a door to your right and left .
        which one do you take?'''

        choice = raw_input(">>")

        if choice == "left":
            bear_room()
        elif choice == "right":
            cthulhu_room()
        else:
            dead("You stumble around the room until you starve")

start()
